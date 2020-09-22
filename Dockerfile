# Prepare the base environment.
FROM python:3.7.8-slim-buster as builder_base
MAINTAINER asi@dbca.wa.gov.au
RUN apt-get update -y \
  && apt-get upgrade -y \
  && apt-get install --no-install-recommends -y gcc binutils python3-dev default-libmysqlclient-dev \
  && rm -rf /var/lib/apt/lists/* \
  && pip install --upgrade pip

# Install Python libs using poetry.
FROM builder_base as python_libs
WORKDIR /app
ENV POETRY_VERSION=1.0.5
RUN pip install "poetry==$POETRY_VERSION"
RUN python -m venv /venv
COPY poetry.lock pyproject.toml /app/
RUN poetry config virtualenvs.create false \
  && poetry install --no-dev --no-interaction --no-ansi

# Install the project.
FROM python_libs
COPY manage.py gunicorn.py ./
COPY glpi ./glpi
COPY glpiconnect ./glpiconnect
RUN python manage.py collectstatic --noinput
# Run the application as the www-data user.
USER www-data
EXPOSE 8080
CMD ["gunicorn", "glpiconnect.wsgi", "--config", "gunicorn.py"]
