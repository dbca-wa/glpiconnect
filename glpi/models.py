# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class GlpiAlerts(models.Model):
    id = models.IntegerField(primary_key=True)
    itemtype = models.CharField(max_length=100)
    items_id = models.IntegerField()
    type = models.IntegerField()
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'glpi_alerts'
        unique_together = ('itemtype', 'items_id', 'type')


class GlpiApiclients(models.Model):
    id = models.IntegerField(primary_key=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    is_active = models.IntegerField()
    ipv4_range_start = models.BigIntegerField(blank=True, null=True)
    ipv4_range_end = models.BigIntegerField(blank=True, null=True)
    ipv6 = models.CharField(max_length=255, blank=True, null=True)
    app_token = models.CharField(max_length=255, blank=True, null=True)
    app_token_date = models.DateTimeField(blank=True, null=True)
    dolog_method = models.IntegerField()
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_apiclients'


class GlpiApplianceenvironments(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_applianceenvironments'


class GlpiAppliancerelations(models.Model):
    id = models.IntegerField(primary_key=True)
    appliances_items = models.ForeignKey('GlpiAppliancesItems', on_delete=models.PROTECT)
    relations_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_appliancerelations'


class GlpiAppliances(models.Model):
    id = models.IntegerField(primary_key=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255)
    is_deleted = models.IntegerField()
    appliancetypes = models.ForeignKey('GlpiAppliancetypes', on_delete=models.PROTECT)
    comment = models.TextField(blank=True, null=True)
    locations = models.ForeignKey('GlpiLocations', on_delete=models.PROTECT)
    manufacturers = models.ForeignKey('GlpiManufacturers', on_delete=models.PROTECT)
    applianceenvironments = models.ForeignKey('GlpiApplianceenvironments', on_delete=models.PROTECT)
    users = models.ForeignKey('GlpiUsers', on_delete=models.PROTECT)
    users_id_tech = models.IntegerField()
    groups = models.ForeignKey('GlpiGroups', on_delete=models.PROTECT)
    groups_id_tech = models.IntegerField()
    relationtype = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    states = models.ForeignKey('GlpiStates', on_delete=models.PROTECT)
    externalidentifier = models.CharField(unique=True, max_length=255, blank=True, null=True)
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_appliances'


class GlpiAppliancesItems(models.Model):
    id = models.IntegerField(primary_key=True)
    appliances = models.ForeignKey('GlpiAppliances', on_delete=models.PROTECT)
    items_id = models.IntegerField()
    itemtype = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'glpi_appliances_items'
        unique_together = ('appliances_id', 'items_id', 'itemtype')


class GlpiAppliancetypes(models.Model):
    id = models.IntegerField(primary_key=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255)
    comment = models.TextField(blank=True, null=True)
    externalidentifier = models.CharField(unique=True, max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_appliancetypes'


class GlpiAuthldapreplicates(models.Model):
    id = models.IntegerField(primary_key=True)
    authldaps = models.ForeignKey('GlpiAuthldaps', on_delete=models.PROTECT)
    host = models.CharField(max_length=255, blank=True, null=True)
    port = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_authldapreplicates'


class GlpiAuthldaps(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    host = models.CharField(max_length=255, blank=True, null=True)
    basedn = models.CharField(max_length=255, blank=True, null=True)
    rootdn = models.CharField(max_length=255, blank=True, null=True)
    port = models.IntegerField()
    condition = models.TextField(blank=True, null=True)
    login_field = models.CharField(max_length=255, blank=True, null=True)
    sync_field = models.CharField(max_length=255, blank=True, null=True)
    use_tls = models.IntegerField()
    group_field = models.CharField(max_length=255, blank=True, null=True)
    group_condition = models.TextField(blank=True, null=True)
    group_search_type = models.IntegerField()
    group_member_field = models.CharField(max_length=255, blank=True, null=True)
    email1_field = models.CharField(max_length=255, blank=True, null=True)
    realname_field = models.CharField(max_length=255, blank=True, null=True)
    firstname_field = models.CharField(max_length=255, blank=True, null=True)
    phone_field = models.CharField(max_length=255, blank=True, null=True)
    phone2_field = models.CharField(max_length=255, blank=True, null=True)
    mobile_field = models.CharField(max_length=255, blank=True, null=True)
    comment_field = models.CharField(max_length=255, blank=True, null=True)
    use_dn = models.IntegerField()
    time_offset = models.IntegerField()
    deref_option = models.IntegerField()
    title_field = models.CharField(max_length=255, blank=True, null=True)
    category_field = models.CharField(max_length=255, blank=True, null=True)
    language_field = models.CharField(max_length=255, blank=True, null=True)
    entity_field = models.CharField(max_length=255, blank=True, null=True)
    entity_condition = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    is_default = models.IntegerField()
    is_active = models.IntegerField()
    rootdn_passwd = models.CharField(max_length=255, blank=True, null=True)
    registration_number_field = models.CharField(max_length=255, blank=True, null=True)
    email2_field = models.CharField(max_length=255, blank=True, null=True)
    email3_field = models.CharField(max_length=255, blank=True, null=True)
    email4_field = models.CharField(max_length=255, blank=True, null=True)
    location_field = models.CharField(max_length=255, blank=True, null=True)
    responsible_field = models.CharField(max_length=255, blank=True, null=True)
    pagesize = models.IntegerField()
    ldap_maxlimit = models.IntegerField()
    can_support_pagesize = models.IntegerField()
    picture_field = models.CharField(max_length=255, blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    inventory_domain = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_authldaps'


class GlpiAuthmails(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    connect_string = models.CharField(max_length=255, blank=True, null=True)
    host = models.CharField(max_length=255, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    is_active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_authmails'


class GlpiAutoupdatesystems(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_autoupdatesystems'


class GlpiBlacklistedmailcontents(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_blacklistedmailcontents'


class GlpiBlacklists(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_blacklists'


class GlpiBudgets(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    is_deleted = models.IntegerField()
    begin_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    value = models.DecimalField(max_digits=20, decimal_places=4)
    is_template = models.IntegerField()
    template_name = models.CharField(max_length=255, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    locations = models.ForeignKey('GlpiLocations', on_delete=models.PROTECT)
    budgettypes = models.ForeignKey('GlpiBudgettypes', on_delete=models.PROTECT)

    class Meta:
        managed = False
        db_table = 'glpi_budgets'


class GlpiBudgettypes(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_budgettypes'


class GlpiBusinesscriticities(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    businesscriticities = models.ForeignKey('self', on_delete=models.PROTECT)
    completename = models.TextField(blank=True, null=True)
    level = models.IntegerField()
    ancestors_cache = models.TextField(blank=True, null=True)
    sons_cache = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_businesscriticities'
        unique_together = (('businesscriticities', 'name'),)


class GlpiCalendars(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    cache_duration = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_calendars'


class GlpiCalendarsHolidays(models.Model):
    id = models.IntegerField(primary_key=True)
    calendars = models.ForeignKey('GlpiCalendars', on_delete=models.PROTECT)
    holidays = models.ForeignKey('GlpiHolidays', on_delete=models.PROTECT)

    class Meta:
        managed = False
        db_table = 'glpi_calendars_holidays'
        unique_together = ('calendars', 'holidays')


class GlpiCalendarsegments(models.Model):
    id = models.IntegerField(primary_key=True)
    calendars = models.ForeignKey('GlpiCalendars', on_delete=models.PROTECT)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    day = models.IntegerField()
    begin = models.TimeField(blank=True, null=True)
    end = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_calendarsegments'


class GlpiCartridgeitems(models.Model):
    id = models.IntegerField(primary_key=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    ref = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey('GlpiLocations', on_delete=models.PROTECT)
    cartridgeitemtypes = models.ForeignKey('GlpiCartridgeitemtypes', on_delete=models.PROTECT)
    manufacturers = models.ForeignKey('GlpiManufacturers', on_delete=models.PROTECT)
    users_id_tech = models.IntegerField()
    groups_id_tech = models.IntegerField()
    is_deleted = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    alarm_threshold = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_cartridgeitems'


class GlpiCartridgeitemsPrintermodels(models.Model):
    id = models.IntegerField(primary_key=True)
    cartridgeitems = models.ForeignKey('GlpiCartridgeitems', on_delete=models.PROTECT)
    printermodels = models.ForeignKey('GlpiPrintermodels', on_delete=models.PROTECT)

    class Meta:
        managed = False
        db_table = 'glpi_cartridgeitems_printermodels'
        unique_together = ('printermodels', 'cartridgeitems')


class GlpiCartridgeitemtypes(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_cartridgeitemtypes'


class GlpiCartridges(models.Model):
    id = models.IntegerField(primary_key=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    cartridgeitems = models.ForeignKey('GlpiCartridgeitems', on_delete=models.PROTECT)
    printers = models.ForeignKey('GlpiPrinters', on_delete=models.PROTECT)
    date_in = models.DateField(blank=True, null=True)
    date_use = models.DateField(blank=True, null=True)
    date_out = models.DateField(blank=True, null=True)
    pages = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_cartridges'


class GlpiCertificates(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    is_deleted = models.IntegerField()
    is_template = models.IntegerField()
    template_name = models.CharField(max_length=255, blank=True, null=True)
    certificatetypes = models.ForeignKey('GlpiCertificatetypes', on_delete=models.PROTECT)
    dns_name = models.CharField(max_length=255, blank=True, null=True)
    dns_suffix = models.CharField(max_length=255, blank=True, null=True)
    users_id_tech = models.IntegerField()
    groups_id_tech = models.IntegerField()
    locations = models.ForeignKey('GlpiLocations', on_delete=models.PROTECT)
    manufacturers = models.ForeignKey('GlpiManufacturers', on_delete=models.PROTECT)
    contact = models.CharField(max_length=255, blank=True, null=True)
    contact_num = models.CharField(max_length=255, blank=True, null=True)
    users = models.ForeignKey('GlpiUsers', on_delete=models.PROTECT)
    groups = models.ForeignKey('GlpiGroups', on_delete=models.PROTECT)
    is_autosign = models.IntegerField()
    date_expiration = models.DateField(blank=True, null=True)
    states = models.ForeignKey('GlpiStates', on_delete=models.PROTECT)
    command = models.TextField(blank=True, null=True)
    certificate_request = models.TextField(blank=True, null=True)
    certificate_item = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_certificates'


class GlpiCertificatesItems(models.Model):
    id = models.IntegerField(primary_key=True)
    certificates = models.ForeignKey('GlpiCertificates', on_delete=models.PROTECT)
    items_id = models.IntegerField()
    itemtype = models.CharField(max_length=100)
    date_creation = models.DateTimeField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_certificates_items'
        unique_together = ('certificates', 'itemtype', 'items_id')


class GlpiCertificatetypes(models.Model):
    id = models.IntegerField(primary_key=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_certificatetypes'


class GlpiChangecosts(models.Model):
    id = models.IntegerField(primary_key=True)
    changes = models.ForeignKey('GlpiChanges', on_delete=models.PROTECT)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    begin_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    actiontime = models.IntegerField()
    cost_time = models.DecimalField(max_digits=20, decimal_places=4)
    cost_fixed = models.DecimalField(max_digits=20, decimal_places=4)
    cost_material = models.DecimalField(max_digits=20, decimal_places=4)
    budgets = models.ForeignKey('GlpiBudgets', on_delete=models.PROTECT)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_changecosts'


class GlpiChanges(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    is_deleted = models.IntegerField()
    status = models.IntegerField()
    content = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    solvedate = models.DateTimeField(blank=True, null=True)
    closedate = models.DateTimeField(blank=True, null=True)
    time_to_resolve = models.DateTimeField(blank=True, null=True)
    users_id_recipient = models.IntegerField()
    users_id_lastupdater = models.IntegerField()
    urgency = models.IntegerField()
    impact = models.IntegerField()
    priority = models.IntegerField()
    itilcategories = models.ForeignKey('GlpiItilcategories', on_delete=models.PROTECT)
    impactcontent = models.TextField(blank=True, null=True)
    controlistcontent = models.TextField(blank=True, null=True)
    rolloutplancontent = models.TextField(blank=True, null=True)
    backoutplancontent = models.TextField(blank=True, null=True)
    checklistcontent = models.TextField(blank=True, null=True)
    global_validation = models.IntegerField()
    validation_percent = models.IntegerField()
    actiontime = models.IntegerField()
    begin_waiting_date = models.DateTimeField(blank=True, null=True)
    waiting_duration = models.IntegerField()
    close_delay_stat = models.IntegerField()
    solve_delay_stat = models.IntegerField()
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_changes'


class GlpiChangesGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    changes = models.ForeignKey('GlpiChanges', on_delete=models.PROTECT)
    groups = models.ForeignKey('GlpiGroups', on_delete=models.PROTECT)
    type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_changes_groups'
        unique_together = ('changes', 'type', 'groups')


class GlpiChangesItems(models.Model):
    id = models.IntegerField(primary_key=True)
    changes = models.ForeignKey('GlpiChanges', on_delete=models.PROTECT)
    itemtype = models.CharField(max_length=100, blank=True, null=True)
    items_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_changes_items'
        unique_together = ('changes', 'itemtype', 'items_id')


class GlpiChangesProblems(models.Model):
    id = models.IntegerField(primary_key=True)
    changes = models.ForeignKey('GlpiChanges', on_delete=models.PROTECT)
    problems = models.ForeignKey('GlpiProblems', on_delete=models.PROTECT)

    class Meta:
        managed = False
        db_table = 'glpi_changes_problems'
        unique_together = ('changes', 'problems')


class GlpiChangesSuppliers(models.Model):
    id = models.IntegerField(primary_key=True)
    changes = models.ForeignKey('GlpiChanges', on_delete=models.PROTECT)
    suppliers = models.ForeignKey('GlpiSuppliers', on_delete=models.PROTECT)
    type = models.IntegerField()
    use_notification = models.IntegerField()
    alternative_email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_changes_suppliers'
        unique_together = ('changes', 'type', 'suppliers')


class GlpiChangesTickets(models.Model):
    id = models.IntegerField(primary_key=True)
    changes = models.ForeignKey('GlpiChanges', on_delete=models.PROTECT)
    tickets = models.ForeignKey('GlpiTickets', on_delete=models.PROTECT)

    class Meta:
        managed = False
        db_table = 'glpi_changes_tickets'
        unique_together = ('changes', 'tickets')


class GlpiChangesUsers(models.Model):
    id = models.IntegerField(primary_key=True)
    changes = models.ForeignKey('GlpiChanges', on_delete=models.PROTECT)
    users = models.ForeignKey('GlpiUsers', on_delete=models.PROTECT)
    type = models.IntegerField()
    use_notification = models.IntegerField()
    alternative_email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_changes_users'
        unique_together = ('changes', 'type', 'users', 'alternative_email')


class GlpiChangetasks(models.Model):
    id = models.IntegerField(primary_key=True)
    uuid = models.CharField(unique=True, max_length=255, blank=True, null=True)
    changes = models.ForeignKey('GlpiChanges', on_delete=models.PROTECT)
    taskcategories = models.ForeignKey('GlpiTaskcategories', on_delete=models.PROTECT)
    state = models.IntegerField()
    date = models.DateTimeField(blank=True, null=True)
    begin = models.DateTimeField(blank=True, null=True)
    end = models.DateTimeField(blank=True, null=True)
    users = models.ForeignKey('GlpiUsers', on_delete=models.PROTECT)
    users_id_editor = models.IntegerField()
    users_id_tech = models.IntegerField()
    groups_id_tech = models.IntegerField()
    content = models.TextField(blank=True, null=True)
    actiontime = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    tasktemplates = models.ForeignKey('GlpiTasktemplates', on_delete=models.PROTECT)
    timeline_position = models.IntegerField()
    is_private = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_changetasks'


class GlpiChangetemplatehiddenfields(models.Model):
    id = models.IntegerField(primary_key=True)
    changetemplates = models.ForeignKey('GlpiChangetemplates', on_delete=models.PROTECT)
    num = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_changetemplatehiddenfields'
        unique_together = ('changetemplates', 'num')


class GlpiChangetemplatemandatoryfields(models.Model):
    id = models.IntegerField(primary_key=True)
    changetemplates = models.ForeignKey('GlpiChangetemplates', on_delete=models.PROTECT)
    num = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_changetemplatemandatoryfields'
        unique_together = ('changetemplates', 'num')


class GlpiChangetemplatepredefinedfields(models.Model):
    id = models.IntegerField(primary_key=True)
    changetemplates = models.ForeignKey('GlpiChangetemplates', on_delete=models.PROTECT)
    num = models.IntegerField()
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_changetemplatepredefinedfields'


class GlpiChangetemplates(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_changetemplates'


class GlpiChangevalidations(models.Model):
    id = models.IntegerField(primary_key=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    users = models.ForeignKey('GlpiUsers', on_delete=models.PROTECT)
    changes = models.ForeignKey('GlpiChanges', on_delete=models.PROTECT)
    users_id_validate = models.IntegerField()
    comment_submission = models.TextField(blank=True, null=True)
    comment_validation = models.TextField(blank=True, null=True)
    status = models.IntegerField()
    submission_date = models.DateTimeField(blank=True, null=True)
    validation_date = models.DateTimeField(blank=True, null=True)
    timeline_position = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_changevalidations'


class GlpiClusters(models.Model):
    id = models.IntegerField(primary_key=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(max_length=255, blank=True, null=True)
    version = models.CharField(max_length=255, blank=True, null=True)
    users_id_tech = models.IntegerField()
    groups_id_tech = models.IntegerField()
    is_deleted = models.IntegerField()
    states = models.ForeignKey('GlpiStates', on_delete=models.PROTECT)
    comment = models.TextField(blank=True, null=True)
    clustertypes = models.ForeignKey('GlpiClustertypes', on_delete=models.PROTECT)
    autoupdatesystems = models.ForeignKey('GlpiAutoupdatesystems', on_delete=models.PROTECT)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_clusters'


class GlpiClustertypes(models.Model):
    id = models.IntegerField(primary_key=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_clustertypes'


class GlpiComputerantiviruses(models.Model):
    id = models.IntegerField(primary_key=True)
    computers = models.ForeignKey('GlpiComputers', on_delete=models.PROTECT)
    name = models.CharField(max_length=255, blank=True, null=True)
    manufacturers = models.ForeignKey('GlpiManufacturers', on_delete=models.PROTECT)
    antivirus_version = models.CharField(max_length=255, blank=True, null=True)
    signature_version = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.IntegerField()
    is_deleted = models.IntegerField()
    is_uptodate = models.IntegerField()
    is_dynamic = models.IntegerField()
    date_expiration = models.DateTimeField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_computerantiviruses'


class GlpiComputermodels(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)
    weight = models.IntegerField()
    required_units = models.IntegerField()
    depth = models.FloatField()
    power_connections = models.IntegerField()
    power_consumption = models.IntegerField()
    is_half_rack = models.IntegerField()
    picture_front = models.TextField(blank=True, null=True)
    picture_rear = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_computermodels'


class GlpiComputers(models.Model):
    id = models.IntegerField(primary_key=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    name = models.CharField(max_length=255, blank=True, null=True)
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    contact = models.CharField(max_length=255, blank=True, null=True)
    contact_num = models.CharField(max_length=255, blank=True, null=True)
    users_id_tech = models.IntegerField()
    groups_id_tech = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    autoupdatesystems = models.ForeignKey('GlpiAutoupdatesystems', on_delete=models.PROTECT)
    locations = models.ForeignKey('GlpiLocations', on_delete=models.PROTECT)
    networks = models.ForeignKey('GlpiNetworks', on_delete=models.PROTECT)
    computermodels = models.ForeignKey('GlpiComputermodels', on_delete=models.PROTECT)
    computertypes = models.ForeignKey('GlpiComputertypes', on_delete=models.PROTECT)
    is_template = models.IntegerField()
    template_name = models.CharField(max_length=255, blank=True, null=True)
    manufacturers = models.ForeignKey('GlpiManufacturers', on_delete=models.PROTECT)
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    users = models.ForeignKey('GlpiUsers', on_delete=models.PROTECT)
    groups = models.ForeignKey('GlpiGroups', on_delete=models.PROTECT)
    states = models.ForeignKey('GlpiStates', on_delete=models.PROTECT)
    ticket_tco = models.DecimalField(max_digits=20, decimal_places=4, blank=True, null=True)
    uuid = models.CharField(max_length=255, blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    is_recursive = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_computers'


class GlpiComputersItems(models.Model):
    id = models.IntegerField(primary_key=True)
    items_id = models.IntegerField()
    computers = models.ForeignKey('GlpiComputers', on_delete=models.PROTECT)
    itemtype = models.CharField(max_length=100)
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_computers_items'


class GlpiComputertypes(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_computertypes'


class GlpiComputervirtualmachines(models.Model):
    id = models.IntegerField(primary_key=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    computers = models.ForeignKey('GlpiComputers', on_delete=models.PROTECT)
    name = models.CharField(max_length=255)
    virtualmachinestates = models.ForeignKey('GlpiStates', on_delete=models.PROTECT)
    virtualmachinesystems = models.ForeignKey('GlpiVirtualmachinesystems', on_delete=models.PROTECT)
    virtualmachinetypes = models.ForeignKey('GlpiVirtualmachinetypes', on_delete=models.PROTECT)
    uuid = models.CharField(max_length=255)
    vcpu = models.IntegerField()
    ram = models.CharField(max_length=255)
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_computervirtualmachines'


class GlpiConfigs(models.Model):
    id = models.IntegerField(primary_key=True)
    context = models.CharField(max_length=150, blank=True, null=True)
    name = models.CharField(max_length=150, blank=True, null=True)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_configs'
        unique_together = (('context', 'name'),)


class GlpiConsumableitems(models.Model):
    id = models.IntegerField(primary_key=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    ref = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey('GlpiLocations', on_delete=models.PROTECT)
    consumableitemtypes = models.ForeignKey('GlpiConsumableitemtypes', on_delete=models.PROTECT)
    manufacturers = models.ForeignKey('GlpiManufacturers', on_delete=models.PROTECT)
    users_id_tech = models.IntegerField()
    groups_id_tech = models.IntegerField()
    is_deleted = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    alarm_threshold = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_consumableitems'


class GlpiConsumableitemtypes(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_consumableitemtypes'


class GlpiConsumables(models.Model):
    id = models.IntegerField(primary_key=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    consumableitems = models.ForeignKey('GlpiConsumableitems', on_delete=models.PROTECT)
    date_in = models.DateField(blank=True, null=True)
    date_out = models.DateField(blank=True, null=True)
    itemtype = models.CharField(max_length=100, blank=True, null=True)
    items_id = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_consumables'


class GlpiContacts(models.Model):
    id = models.IntegerField(primary_key=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    firstname = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    phone2 = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=255, blank=True, null=True)
    fax = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    contacttypes = models.ForeignKey('GlpiContacttypes', on_delete=models.PROTECT)
    comment = models.TextField(blank=True, null=True)
    is_deleted = models.IntegerField()
    usertitles = models.ForeignKey('GlpiUsertitles', on_delete=models.PROTECT)
    address = models.TextField(blank=True, null=True)
    postcode = models.CharField(max_length=255, blank=True, null=True)
    town = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_contacts'


class GlpiContactsSuppliers(models.Model):
    id = models.IntegerField(primary_key=True)
    suppliers = models.ForeignKey('GlpiSuppliers', on_delete=models.PROTECT)
    contacts = models.ForeignKey('GlpiContacts', on_delete=models.PROTECT)

    class Meta:
        managed = False
        db_table = 'glpi_contacts_suppliers'
        unique_together = ('suppliers', 'contacts')


class GlpiContacttypes(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_contacttypes'


class GlpiContractcosts(models.Model):
    id = models.IntegerField(primary_key=True)
    contracts = models.ForeignKey('GlpiContracts', on_delete=models.PROTECT)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    begin_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    cost = models.DecimalField(max_digits=20, decimal_places=4)
    budgets = models.ForeignKey('GlpiBudgets', on_delete=models.PROTECT)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_contractcosts'


class GlpiContracts(models.Model):
    id = models.IntegerField(primary_key=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    num = models.CharField(max_length=255, blank=True, null=True)
    contracttypes = models.ForeignKey('GlpiContracttypes', on_delete=models.PROTECT)
    begin_date = models.DateField(blank=True, null=True)
    duration = models.IntegerField()
    notice = models.IntegerField()
    periodicity = models.IntegerField()
    billing = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    accounting_number = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.IntegerField()
    week_begin_hour = models.TimeField()
    week_end_hour = models.TimeField()
    saturday_begin_hour = models.TimeField()
    saturday_end_hour = models.TimeField()
    use_saturday = models.IntegerField()
    monday_begin_hour = models.TimeField()
    monday_end_hour = models.TimeField()
    use_monday = models.IntegerField()
    max_links_allowed = models.IntegerField()
    alert = models.IntegerField()
    renewal = models.IntegerField()
    template_name = models.CharField(max_length=255, blank=True, null=True)
    is_template = models.IntegerField()
    states = models.ForeignKey('GlpiStates', on_delete=models.PROTECT)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_contracts'


class GlpiContractsItems(models.Model):
    id = models.IntegerField(primary_key=True)
    contracts = models.ForeignKey('GlpiContracts', on_delete=models.PROTECT)
    items_id = models.IntegerField()
    itemtype = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'glpi_contracts_items'
        unique_together = ('contracts', 'itemtype', 'items_id')


class GlpiContractsSuppliers(models.Model):
    id = models.IntegerField(primary_key=True)
    suppliers = models.ForeignKey('GlpiSuppliers', on_delete=models.PROTECT)
    contracts = models.ForeignKey('GlpiContracts', on_delete=models.PROTECT)

    class Meta:
        managed = False
        db_table = 'glpi_contracts_suppliers'
        unique_together = ('suppliers', 'contracts')


class GlpiContracttypes(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_contracttypes'


class GlpiCrontasklogs(models.Model):
    id = models.IntegerField(primary_key=True)
    crontasks = models.ForeignKey('GlpiCrontasks', on_delete=models.PROTECT)
    crontasklogs = models.ForeignKey('GlpiCrontasklogs', on_delete=models.PROTECT)
    date = models.DateTimeField()
    state = models.IntegerField()
    elapsed = models.FloatField()
    volume = models.IntegerField()
    content = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_crontasklogs'


class GlpiCrontasks(models.Model):
    id = models.IntegerField(primary_key=True)
    itemtype = models.CharField(max_length=100)
    name = models.CharField(max_length=150)
    frequency = models.IntegerField()
    param = models.IntegerField(blank=True, null=True)
    state = models.IntegerField()
    mode = models.IntegerField()
    allowmode = models.IntegerField()
    hourmin = models.IntegerField()
    hourmax = models.IntegerField()
    logs_lifetime = models.IntegerField()
    lastrun = models.DateTimeField(blank=True, null=True)
    lastcode = models.IntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_crontasks'
        unique_together = (('itemtype', 'name'),)


class GlpiDashboardsDashboards(models.Model):
    id = models.IntegerField(primary_key=True)
    key = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=100)
    context = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'glpi_dashboards_dashboards'


class GlpiDashboardsItems(models.Model):
    id = models.IntegerField(primary_key=True)
    dashboards_dashboards_id = models.IntegerField()
    gridstack_id = models.CharField(max_length=100)
    card_id = models.CharField(max_length=100)
    x = models.IntegerField(blank=True, null=True)
    y = models.IntegerField(blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    card_options = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_dashboards_items'


class GlpiDashboardsRights(models.Model):
    id = models.IntegerField(primary_key=True)
    dashboards_dashboards_id = models.IntegerField()
    itemtype = models.CharField(max_length=100)
    items_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_dashboards_rights'
        unique_together = ('dashboards_dashboards_id', 'itemtype', 'items_id')


class GlpiDatacenters(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    locations = models.ForeignKey('GlpiLocations', on_delete=models.PROTECT)
    is_deleted = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_datacenters'


class GlpiDcrooms(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    locations = models.ForeignKey('GlpiLocations', on_delete=models.PROTECT)
    vis_cols = models.IntegerField(blank=True, null=True)
    vis_rows = models.IntegerField(blank=True, null=True)
    blueprint = models.TextField(blank=True, null=True)
    datacenters = models.ForeignKey('GlpiDatacenters', on_delete=models.PROTECT)
    is_deleted = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_dcrooms'


class GlpiDevicebatteries(models.Model):
    id = models.IntegerField(primary_key=True)
    designation = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    manufacturers = models.ForeignKey('GlpiManufacturers', on_delete=models.PROTECT)
    voltage = models.IntegerField(blank=True, null=True)
    capacity = models.IntegerField(blank=True, null=True)
    devicebatterytypes = models.ForeignKey('GlpiDevicebatterytypes', on_delete=models.PROTECT)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    devicebatterymodels = models.ForeignKey('GlpiDevicebatterymodels', on_delete=models.SET_NULL, null=True, blank=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicebatteries'


class GlpiDevicebatterymodels(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicebatterymodels'


class GlpiDevicebatterytypes(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicebatterytypes'


class GlpiDevicecasemodels(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicecasemodels'


class GlpiDevicecases(models.Model):
    id = models.IntegerField(primary_key=True)
    designation = models.CharField(max_length=255, blank=True, null=True)
    devicecasetypes = models.ForeignKey('GlpiDevicecasetypes', on_delete=models.PROTECT)
    comment = models.TextField(blank=True, null=True)
    manufacturers = models.ForeignKey('GlpiManufacturers', on_delete=models.PROTECT)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    devicecasemodels = models.ForeignKey('GlpiDevicecasemodels', on_delete=models.SET_NULL, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicecases'


class GlpiDevicecasetypes(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicecasetypes'


class GlpiDevicecontrolmodels(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicecontrolmodels'


class GlpiDevicecontrols(models.Model):
    id = models.IntegerField(primary_key=True)
    designation = models.CharField(max_length=255, blank=True, null=True)
    is_raid = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    manufacturers = models.ForeignKey('GlpiManufacturers', on_delete=models.PROTECT)
    interfacetypes = models.ForeignKey('GlpiInterfacetypes', on_delete=models.PROTECT)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    devicecontrolmodels = models.ForeignKey('GlpiDevicecontrolmodels', on_delete=models.SET_NULL, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicecontrols'


class GlpiDevicedrivemodels(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicedrivemodels'


class GlpiDevicedrives(models.Model):
    id = models.IntegerField(primary_key=True)
    designation = models.CharField(max_length=255, blank=True, null=True)
    is_writer = models.IntegerField()
    speed = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    manufacturers = models.ForeignKey('GlpiManufacturers', on_delete=models.PROTECT)
    interfacetypes = models.ForeignKey('GlpiInterfacetypes', on_delete=models.PROTECT)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    devicedrivemodels = models.ForeignKey('GlpiDevicedrivemodels', on_delete=models.SET_NULL, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicedrives'


class GlpiDevicefirmwaremodels(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicefirmwaremodels'


class GlpiDevicefirmwares(models.Model):
    id = models.IntegerField(primary_key=True)
    designation = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    manufacturers = models.ForeignKey('GlpiManufacturers', on_delete=models.PROTECT)
    date = models.DateField(blank=True, null=True)
    version = models.CharField(max_length=255, blank=True, null=True)
    devicefirmwaretypes = models.ForeignKey('GlpiDevicefirmwaretypes', on_delete=models.PROTECT)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    devicefirmwaremodels = models.ForeignKey('GlpiDevicefirmwaremodels', on_delete=models.SET_NULL, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicefirmwares'


class GlpiDevicefirmwaretypes(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicefirmwaretypes'


class GlpiDevicegenericmodels(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicegenericmodels'


class GlpiDevicegenerics(models.Model):
    id = models.IntegerField(primary_key=True)
    designation = models.CharField(max_length=255, blank=True, null=True)
    devicegenerictypes = models.ForeignKey('GlpiDevicegenerictypes', on_delete=models.PROTECT)
    comment = models.TextField(blank=True, null=True)
    manufacturers = models.ForeignKey('GlpiManufacturers', on_delete=models.PROTECT)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    locations = models.ForeignKey('GlpiLocations', on_delete=models.PROTECT)
    states = models.ForeignKey('GlpiStates', on_delete=models.PROTECT)
    devicegenericmodels = models.ForeignKey('GlpiDevicegenericmodels', on_delete=models.SET_NULL, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicegenerics'


class GlpiDevicegenerictypes(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicegenerictypes'


class GlpiDevicegraphiccardmodels(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicegraphiccardmodels'


class GlpiDevicegraphiccards(models.Model):
    id = models.IntegerField(primary_key=True)
    designation = models.CharField(max_length=255, blank=True, null=True)
    interfacetypes = models.ForeignKey('GlpiInterfacetypes', on_delete=models.PROTECT)
    comment = models.TextField(blank=True, null=True)
    manufacturers = models.ForeignKey('GlpiManufacturers', on_delete=models.PROTECT)
    memory_default = models.IntegerField()
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    devicegraphiccardmodels = models.ForeignKey('GlpiDevicegraphiccardmodels', on_delete=models.SET_NULL, blank=True, null=True)
    chipset = models.CharField(max_length=255, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicegraphiccards'


class GlpiDeviceharddrivemodels(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_deviceharddrivemodels'


class GlpiDeviceharddrives(models.Model):
    id = models.IntegerField(primary_key=True)
    designation = models.CharField(max_length=255, blank=True, null=True)
    rpm = models.CharField(max_length=255, blank=True, null=True)
    interfacetypes = models.ForeignKey('GlpiInterfacetypes', on_delete=models.PROTECT)
    cache = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    manufacturers = models.ForeignKey('GlpiManufacturers', on_delete=models.PROTECT)
    capacity_default = models.IntegerField()
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    deviceharddrivemodels = models.ForeignKey('GlpiDeviceharddrivemodels', on_delete=models.SET_NULL, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_deviceharddrives'


class GlpiDevicememories(models.Model):
    id = models.IntegerField(primary_key=True)
    designation = models.CharField(max_length=255, blank=True, null=True)
    frequence = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    manufacturers = models.ForeignKey('GlpiManufacturers', on_delete=models.PROTECT)
    size_default = models.IntegerField()
    devicememorytypes = models.ForeignKey('GlpiDevicememorytypes', on_delete=models.PROTECT)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    devicememorymodels = models.ForeignKey('GlpiDevicememorymodels', on_delete=models.SET_NULL, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicememories'


class GlpiDevicememorymodels(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicememorymodels'


class GlpiDevicememorytypes(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicememorytypes'


class GlpiDevicemotherboardmodels(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicemotherboardmodels'


class GlpiDevicemotherboards(models.Model):
    id = models.IntegerField(primary_key=True)
    designation = models.CharField(max_length=255, blank=True, null=True)
    chipset = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    manufacturers = models.ForeignKey('GlpiManufacturers', on_delete=models.PROTECT)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    devicemotherboardmodels = models.ForeignKey('GlpiDevicemotherboardmodels', on_delete=models.SET_NULL, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicemotherboards'


class GlpiDevicenetworkcardmodels(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicenetworkcardmodels'


class GlpiDevicenetworkcards(models.Model):
    id = models.IntegerField(primary_key=True)
    designation = models.CharField(max_length=255, blank=True, null=True)
    bandwidth = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    manufacturers = models.ForeignKey('GlpiManufacturers', on_delete=models.PROTECT)
    mac_default = models.CharField(max_length=255, blank=True, null=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    devicenetworkcardmodels = models.ForeignKey('GlpiDevicenetworkcardmodels', on_delete=models.SET_NULL, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicenetworkcards'


class GlpiDevicepcimodels(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicepcimodels'


class GlpiDevicepcis(models.Model):
    id = models.IntegerField(primary_key=True)
    designation = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    manufacturers = models.ForeignKey('GlpiManufacturers', on_delete=models.PROTECT)
    devicenetworkcardmodels = models.ForeignKey('GlpiDevicenetworkcardmodels', on_delete=models.PROTECT)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    devicepcimodels = models.ForeignKey('GlpiDevicepcimodels', on_delete=models.SET_NULL, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicepcis'


class GlpiDevicepowersupplies(models.Model):
    id = models.IntegerField(primary_key=True)
    designation = models.CharField(max_length=255, blank=True, null=True)
    power = models.CharField(max_length=255, blank=True, null=True)
    is_atx = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    manufacturers = models.ForeignKey('GlpiManufacturers', on_delete=models.PROTECT)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    devicepowersupplymodels = models.ForeignKey('GlpiDevicepowersupplymodels', on_delete=models.SET_NULL, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicepowersupplies'


class GlpiDevicepowersupplymodels(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicepowersupplymodels'


class GlpiDeviceprocessormodels(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_deviceprocessormodels'


class GlpiDeviceprocessors(models.Model):
    id = models.IntegerField(primary_key=True)
    designation = models.CharField(max_length=255, blank=True, null=True)
    frequence = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    manufacturers = models.ForeignKey('GlpiManufacturers', on_delete=models.PROTECT)
    frequency_default = models.IntegerField()
    nbcores_default = models.IntegerField(blank=True, null=True)
    nbthreads_default = models.IntegerField(blank=True, null=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    deviceprocessormodels = models.ForeignKey('GlpiDeviceprocessormodels', on_delete=models.SET_NULL, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_deviceprocessors'


class GlpiDevicesensormodels(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicesensormodels'


class GlpiDevicesensors(models.Model):
    id = models.IntegerField(primary_key=True)
    designation = models.CharField(max_length=255, blank=True, null=True)
    devicesensortypes = models.ForeignKey('GlpiDevicesensortypes', on_delete=models.PROTECT)
    devicesensormodels = models.ForeignKey('GlpiDevicesensormodels', on_delete=models.PROTECT)
    comment = models.TextField(blank=True, null=True)
    manufacturers = models.ForeignKey('GlpiManufacturers', on_delete=models.PROTECT)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    locations = models.ForeignKey('GlpiLocations', on_delete=models.PROTECT)
    states = models.ForeignKey('GlpiStates', on_delete=models.PROTECT)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicesensors'


class GlpiDevicesensortypes(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicesensortypes'


class GlpiDevicesimcards(models.Model):
    id = models.IntegerField(primary_key=True)
    designation = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    manufacturers = models.ForeignKey('GlpiManufacturers', on_delete=models.PROTECT)
    voltage = models.IntegerField(blank=True, null=True)
    devicesimcardtypes = models.ForeignKey('GlpiDevicesimcardtypes', on_delete=models.PROTECT)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    allow_voip = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_devicesimcards'


class GlpiDevicesimcardtypes(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicesimcardtypes'


class GlpiDevicesoundcardmodels(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicesoundcardmodels'


class GlpiDevicesoundcards(models.Model):
    id = models.IntegerField(primary_key=True)
    designation = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    manufacturers = models.ForeignKey('GlpiManufacturers', on_delete=models.PROTECT)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    devicesoundcardmodels = models.ForeignKey('GlpiDevicesoundcardmodels', on_delete=models.SET_NULL, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_devicesoundcards'


class GlpiDisplaypreferences(models.Model):
    id = models.IntegerField(primary_key=True)
    itemtype = models.CharField(max_length=100)
    num = models.IntegerField()
    rank = models.IntegerField()
    users = models.ForeignKey('GlpiUsers', on_delete=models.PROTECT)

    class Meta:
        managed = False
        db_table = 'glpi_displaypreferences'
        unique_together = ('users', 'itemtype', 'num')


class GlpiDocumentcategories(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    documentcategories = models.ForeignKey('self', on_delete=models.PROTECT)
    completename = models.TextField(blank=True, null=True)
    level = models.IntegerField()
    ancestors_cache = models.TextField(blank=True, null=True)
    sons_cache = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_documentcategories'
        unique_together = ('documentcategories', 'name')


class GlpiDocuments(models.Model):
    id = models.IntegerField(primary_key=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    filename = models.CharField(max_length=255, blank=True, null=True)
    filepath = models.CharField(max_length=255, blank=True, null=True)
    documentcategories = models.ForeignKey('GlpiDocumentcategories', on_delete=models.PROTECT)
    mime = models.CharField(max_length=255, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    is_deleted = models.IntegerField()
    link = models.CharField(max_length=255, blank=True, null=True)
    users = models.ForeignKey('GlpiUsers', on_delete=models.PROTECT)
    tickets = models.ForeignKey('GlpiTickets', on_delete=models.PROTECT)
    sha1sum = models.CharField(max_length=40, blank=True, null=True)
    is_blacklisted = models.IntegerField()
    tag = models.CharField(max_length=255, blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_documents'


class GlpiDocumentsItems(models.Model):
    id = models.IntegerField(primary_key=True)
    documents = models.ForeignKey('GlpiDocuments', on_delete=models.PROTECT)
    items_id = models.IntegerField()
    itemtype = models.CharField(max_length=100)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    users = models.ForeignKey('GlpiUsers', on_delete=models.PROTECT)
    timeline_position = models.IntegerField()
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_documents_items'
        unique_together = ('documents', 'itemtype', 'items_id', 'timeline_position')


class GlpiDocumenttypes(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    ext = models.CharField(unique=True, max_length=255, blank=True, null=True)
    icon = models.CharField(max_length=255, blank=True, null=True)
    mime = models.CharField(max_length=255, blank=True, null=True)
    is_uploadable = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_documenttypes'


class GlpiDomainrecords(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    domains = models.ForeignKey('GlpiDomains', on_delete=models.PROTECT)
    domainrecordtypes = models.ForeignKey('GlpiDomainrecordtypes', on_delete=models.PROTECT)
    ttl = models.IntegerField()
    users_id_tech = models.IntegerField()
    groups_id_tech = models.IntegerField()
    is_deleted = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_domainrecords'


class GlpiDomainrecordtypes(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_domainrecordtypes'


class GlpiDomainrelations(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_domainrelations'


class GlpiDomains(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    domaintypes = models.ForeignKey('GlpiDomaintypes', on_delete=models.PROTECT)
    date_expiration = models.DateTimeField(blank=True, null=True)
    users_id_tech = models.IntegerField()
    groups_id_tech = models.IntegerField()
    others = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_domains'


class GlpiDomainsItems(models.Model):
    id = models.IntegerField(primary_key=True)
    domains = models.ForeignKey('GlpiDomains', on_delete=models.PROTECT)
    items_id = models.IntegerField()
    itemtype = models.CharField(max_length=100)
    domainrelations = models.ForeignKey('GlpiDomainrelations', on_delete=models.PROTECT)

    class Meta:
        managed = False
        db_table = 'glpi_domains_items'
        unique_together = ('domains', 'itemtype', 'items_id')


class GlpiDomaintypes(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_domaintypes'


class GlpiDropdowntranslations(models.Model):
    id = models.IntegerField(primary_key=True)
    items_id = models.IntegerField()
    itemtype = models.CharField(max_length=100, blank=True, null=True)
    language = models.CharField(max_length=10, blank=True, null=True)
    field = models.CharField(max_length=100, blank=True, null=True)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_dropdowntranslations'
        unique_together = ('itemtype', 'items_id', 'language', 'field')


class GlpiEnclosuremodels(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)
    weight = models.IntegerField()
    required_units = models.IntegerField()
    depth = models.FloatField()
    power_connections = models.IntegerField()
    power_consumption = models.IntegerField()
    is_half_rack = models.IntegerField()
    picture_front = models.TextField(blank=True, null=True)
    picture_rear = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_enclosuremodels'


class GlpiEnclosures(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    locations = models.ForeignKey('GlpiLocations', on_delete=models.PROTECT)
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    enclosuremodels = models.ForeignKey('GlpiEnclosuremodels', on_delete=models.SET_NULL, blank=True, null=True)
    users_id_tech = models.IntegerField()
    groups_id_tech = models.IntegerField()
    is_template = models.IntegerField()
    template_name = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.IntegerField()
    orientation = models.IntegerField(blank=True, null=True)
    power_supplies = models.IntegerField()
    states = models.ForeignKey('GlpiStates', on_delete=models.PROTECT)
    comment = models.TextField(blank=True, null=True)
    manufacturers = models.ForeignKey('GlpiManufacturers', on_delete=models.PROTECT)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_enclosures'


class GlpiEntities(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    completename = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    level = models.IntegerField()
    sons_cache = models.TextField(blank=True, null=True)
    ancestors_cache = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    postcode = models.CharField(max_length=255, blank=True, null=True)
    town = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    phonenumber = models.CharField(max_length=255, blank=True, null=True)
    fax = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    admin_email = models.CharField(max_length=255, blank=True, null=True)
    admin_email_name = models.CharField(max_length=255, blank=True, null=True)
    admin_reply = models.CharField(max_length=255, blank=True, null=True)
    admin_reply_name = models.CharField(max_length=255, blank=True, null=True)
    notification_subject_tag = models.CharField(max_length=255, blank=True, null=True)
    ldap_dn = models.CharField(max_length=255, blank=True, null=True)
    tag = models.CharField(max_length=255, blank=True, null=True)
    authldaps = models.ForeignKey('GlpiAuthldaps', on_delete=models.PROTECT)
    mail_domain = models.CharField(max_length=255, blank=True, null=True)
    entity_ldapfilter = models.TextField(blank=True, null=True)
    mailing_signature = models.TextField(blank=True, null=True)
    cartridges_alert_repeat = models.IntegerField()
    consumables_alert_repeat = models.IntegerField()
    use_licenses_alert = models.IntegerField()
    send_licenses_alert_before_delay = models.IntegerField()
    use_certificates_alert = models.IntegerField()
    send_certificates_alert_before_delay = models.IntegerField()
    use_contracts_alert = models.IntegerField()
    send_contracts_alert_before_delay = models.IntegerField()
    use_infocoms_alert = models.IntegerField()
    send_infocoms_alert_before_delay = models.IntegerField()
    use_reservations_alert = models.IntegerField()
    use_domains_alert = models.IntegerField()
    send_domains_alert_close_expiries_delay = models.IntegerField()
    send_domains_alert_expired_delay = models.IntegerField()
    autoclose_delay = models.IntegerField()
    autopurge_delay = models.IntegerField()
    notclosed_delay = models.IntegerField()
    calendars = models.ForeignKey('GlpiCalendars', on_delete=models.PROTECT)
    auto_assign_mode = models.IntegerField()
    tickettype = models.IntegerField()
    max_closedate = models.DateTimeField(blank=True, null=True)
    inquest_config = models.IntegerField()
    inquest_rate = models.IntegerField()
    inquest_delay = models.IntegerField()
    inquest_url = models.CharField(db_column='inquest_URL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    autofill_warranty_date = models.CharField(max_length=255)
    autofill_use_date = models.CharField(max_length=255)
    autofill_buy_date = models.CharField(max_length=255)
    autofill_delivery_date = models.CharField(max_length=255)
    autofill_order_date = models.CharField(max_length=255)
    tickettemplates = models.ForeignKey('GlpiTickettemplates', on_delete=models.PROTECT)
    changetemplates = models.ForeignKey('GlpiChangetemplates', on_delete=models.PROTECT)
    problemtemplates = models.ForeignKey('GlpiProblemtemplates', on_delete=models.PROTECT)
    entities_id_software = models.IntegerField()
    default_contract_alert = models.IntegerField()
    default_infocom_alert = models.IntegerField()
    default_cartridges_alarm_threshold = models.IntegerField()
    default_consumables_alarm_threshold = models.IntegerField()
    delay_send_emails = models.IntegerField()
    is_notif_enable_default = models.IntegerField()
    inquest_duration = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    autofill_decommission_date = models.CharField(max_length=255)
    suppliers_as_private = models.IntegerField()
    anonymize_support_agents = models.IntegerField()
    enable_custom_css = models.IntegerField()
    custom_css_code = models.TextField(blank=True, null=True)
    latitude = models.CharField(max_length=255, blank=True, null=True)
    longitude = models.CharField(max_length=255, blank=True, null=True)
    altitude = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_entities'
        unique_together = ('entities', 'name')


class GlpiEntitiesKnowbaseitems(models.Model):
    id = models.IntegerField(primary_key=True)
    knowbaseitems = models.ForeignKey('GlpiKnowbaseitems', on_delete=models.PROTECT)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_entities_knowbaseitems'


class GlpiEntitiesReminders(models.Model):
    id = models.IntegerField(primary_key=True)
    reminders = models.ForeignKey('GlpiReminders', on_delete=models.PROTECT)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_entities_reminders'


class GlpiEntitiesRssfeeds(models.Model):
    id = models.IntegerField(primary_key=True)
    rssfeeds = models.ForeignKey('GlpiRssfeeds', on_delete=models.PROTECT)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_entities_rssfeeds'


class GlpiEvents(models.Model):
    id = models.IntegerField(primary_key=True)
    items_id = models.IntegerField()
    type = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    service = models.CharField(max_length=255, blank=True, null=True)
    level = models.IntegerField()
    message = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_events'


class GlpiFieldblacklists(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    field = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    itemtype = models.CharField(max_length=255)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_fieldblacklists'


class GlpiFieldunicities(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    is_recursive = models.IntegerField()
    itemtype = models.CharField(max_length=255)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    fields = models.TextField(blank=True, null=True)
    is_active = models.IntegerField()
    action_refuse = models.IntegerField()
    action_notify = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_fieldunicities'


class GlpiFilesystems(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_filesystems'


class GlpiFqdns(models.Model):
    id = models.IntegerField(primary_key=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    fqdn = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_fqdns'


class GlpiGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    ldap_field = models.CharField(max_length=255, blank=True, null=True)
    ldap_value = models.TextField(blank=True, null=True)
    ldap_group_dn = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    groups = models.ForeignKey('GlpiGroups', on_delete=models.PROTECT)
    completename = models.TextField(blank=True, null=True)
    level = models.IntegerField()
    ancestors_cache = models.TextField(blank=True, null=True)
    sons_cache = models.TextField(blank=True, null=True)
    is_requester = models.IntegerField()
    is_watcher = models.IntegerField()
    is_assign = models.IntegerField()
    is_task = models.IntegerField()
    is_notify = models.IntegerField()
    is_itemgroup = models.IntegerField()
    is_usergroup = models.IntegerField()
    is_manager = models.IntegerField()
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_groups'


class GlpiGroupsKnowbaseitems(models.Model):
    id = models.IntegerField(primary_key=True)
    knowbaseitems = models.ForeignKey('GlpiKnowbaseitems', on_delete=models.PROTECT)
    groups = models.ForeignKey('GlpiGroups', on_delete=models.PROTECT)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_groups_knowbaseitems'


class GlpiGroupsProblems(models.Model):
    id = models.IntegerField(primary_key=True)
    problems = models.ForeignKey('GlpiProblems', on_delete=models.PROTECT)
    groups = models.ForeignKey('GlpiGroups', on_delete=models.PROTECT)
    type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_groups_problems'
        unique_together = ('problems', 'type', 'groups')


class GlpiGroupsReminders(models.Model):
    id = models.IntegerField(primary_key=True)
    reminders = models.ForeignKey('GlpiReminders', on_delete=models.PROTECT)
    groups = models.ForeignKey('GlpiGroups', on_delete=models.PROTECT)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_groups_reminders'


class GlpiGroupsRssfeeds(models.Model):
    id = models.IntegerField(primary_key=True)
    rssfeeds = models.ForeignKey('GlpiRssfeeds', on_delete=models.PROTECT)
    groups = models.ForeignKey('GlpiGroups', on_delete=models.PROTECT)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_groups_rssfeeds'


class GlpiGroupsTickets(models.Model):
    id = models.IntegerField(primary_key=True)
    tickets = models.ForeignKey('GlpiTickets', on_delete=models.PROTECT)
    groups = models.ForeignKey('GlpiGroups', on_delete=models.PROTECT)
    type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_groups_tickets'
        unique_together = ('tickets', 'type', 'groups')


class GlpiGroupsUsers(models.Model):
    id = models.IntegerField(primary_key=True)
    users = models.ForeignKey('GlpiUsers', on_delete=models.PROTECT)
    groups = models.ForeignKey('GlpiGroups', on_delete=models.PROTECT)
    is_dynamic = models.IntegerField()
    is_manager = models.IntegerField()
    is_userdelegate = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_groups_users'
        unique_together = ('users', 'groups')


class GlpiHolidays(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    begin_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    is_perpetual = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_holidays'


class GlpiImpactcompounds(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'glpi_impactcompounds'


class GlpiImpactcontexts(models.Model):
    id = models.IntegerField(primary_key=True)
    positions = models.TextField()
    zoom = models.FloatField()
    pan_x = models.FloatField()
    pan_y = models.FloatField()
    impact_color = models.CharField(max_length=255)
    depends_color = models.CharField(max_length=255)
    impact_and_depends_color = models.CharField(max_length=255)
    show_depends = models.IntegerField()
    show_impact = models.IntegerField()
    max_depth = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_impactcontexts'


class GlpiImpactitems(models.Model):
    id = models.IntegerField(primary_key=True)
    itemtype = models.CharField(max_length=255)
    items_id = models.IntegerField()
    parent_id = models.IntegerField()
    impactcontexts_id = models.IntegerField()
    is_slave = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_impactitems'
        unique_together = ('itemtype', 'items_id')


class GlpiImpactrelations(models.Model):
    id = models.IntegerField(primary_key=True)
    itemtype_source = models.CharField(max_length=255)
    items_id_source = models.IntegerField()
    itemtype_impacted = models.CharField(max_length=255)
    items_id_impacted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_impactrelations'
        unique_together = (('itemtype_source', 'items_id_source', 'itemtype_impacted', 'items_id_impacted'),)


class GlpiInfocoms(models.Model):
    id = models.IntegerField(primary_key=True)
    items_id = models.IntegerField()
    itemtype = models.CharField(max_length=100)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    buy_date = models.DateField(blank=True, null=True)
    use_date = models.DateField(blank=True, null=True)
    warranty_duration = models.IntegerField()
    warranty_info = models.CharField(max_length=255, blank=True, null=True)
    suppliers = models.ForeignKey('GlpiSuppliers', on_delete=models.PROTECT)
    order_number = models.CharField(max_length=255, blank=True, null=True)
    delivery_number = models.CharField(max_length=255, blank=True, null=True)
    immo_number = models.CharField(max_length=255, blank=True, null=True)
    value = models.DecimalField(max_digits=20, decimal_places=4)
    warranty_value = models.DecimalField(max_digits=20, decimal_places=4)
    sink_time = models.IntegerField()
    sink_type = models.IntegerField()
    sink_coeff = models.FloatField()
    comment = models.TextField(blank=True, null=True)
    bill = models.CharField(max_length=255, blank=True, null=True)
    budgets = models.ForeignKey('GlpiBudgets', on_delete=models.PROTECT)
    alert = models.IntegerField()
    order_date = models.DateField(blank=True, null=True)
    delivery_date = models.DateField(blank=True, null=True)
    inventory_date = models.DateField(blank=True, null=True)
    warranty_date = models.DateField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    decommission_date = models.DateTimeField(blank=True, null=True)
    businesscriticities = models.ForeignKey('GlpiBusinesscriticities', on_delete=models.PROTECT)

    class Meta:
        managed = False
        db_table = 'glpi_infocoms'
        unique_together = (('itemtype', 'items_id'),)


class GlpiInterfacetypes(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_interfacetypes'


class GlpiIpaddresses(models.Model):
    id = models.IntegerField(primary_key=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    items_id = models.IntegerField()
    itemtype = models.CharField(max_length=100)
    version = models.PositiveIntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    binary_0 = models.PositiveIntegerField()
    binary_1 = models.PositiveIntegerField()
    binary_2 = models.PositiveIntegerField()
    binary_3 = models.PositiveIntegerField()
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    mainitems_id = models.IntegerField()
    mainitemtype = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_ipaddresses'


class GlpiIpaddressesIpnetworks(models.Model):
    id = models.IntegerField(primary_key=True)
    ipaddresses = models.ForeignKey('GlpiIpaddresses', on_delete=models.PROTECT)
    ipnetworks = models.ForeignKey('GlpiNetworks', on_delete=models.PROTECT)

    class Meta:
        managed = False
        db_table = 'glpi_ipaddresses_ipnetworks'
        unique_together = ('ipaddresses', 'ipnetworks')


class GlpiIpnetworks(models.Model):
    id = models.IntegerField(primary_key=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    ipnetworks = models.ForeignKey('GlpiNetworks', on_delete=models.PROTECT)
    completename = models.TextField(blank=True, null=True)
    level = models.IntegerField()
    ancestors_cache = models.TextField(blank=True, null=True)
    sons_cache = models.TextField(blank=True, null=True)
    addressable = models.IntegerField()
    version = models.PositiveIntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=40, blank=True, null=True)
    address_0 = models.PositiveIntegerField()
    address_1 = models.PositiveIntegerField()
    address_2 = models.PositiveIntegerField()
    address_3 = models.PositiveIntegerField()
    netmask = models.CharField(max_length=40, blank=True, null=True)
    netmask_0 = models.PositiveIntegerField()
    netmask_1 = models.PositiveIntegerField()
    netmask_2 = models.PositiveIntegerField()
    netmask_3 = models.PositiveIntegerField()
    gateway = models.CharField(max_length=40, blank=True, null=True)
    gateway_0 = models.PositiveIntegerField()
    gateway_1 = models.PositiveIntegerField()
    gateway_2 = models.PositiveIntegerField()
    gateway_3 = models.PositiveIntegerField()
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_ipnetworks'


class GlpiIpnetworksVlans(models.Model):
    id = models.IntegerField(primary_key=True)
    ipnetworks = models.ForeignKey('GlpiNetworks', on_delete=models.PROTECT)
    vlans = models.ForeignKey('GlpiVlans', on_delete=models.PROTECT)

    class Meta:
        managed = False
        db_table = 'glpi_ipnetworks_vlans'
        unique_together = ('ipnetworks', 'vlans')


class GlpiItemsClusters(models.Model):
    id = models.IntegerField(primary_key=True)
    clusters = models.ForeignKey('GlpiClusters', on_delete=models.PROTECT)
    itemtype = models.CharField(max_length=100, blank=True, null=True)
    items_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_items_clusters'
        unique_together = ('clusters', 'itemtype', 'items_id')


class GlpiItemsDevicebatteries(models.Model):
    id = models.IntegerField(primary_key=True)
    items_id = models.IntegerField()
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    devicebatteries = models.ForeignKey('GlpiDevicebatteries', on_delete=models.PROTECT)
    manufacturing_date = models.DateField(blank=True, null=True)
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey('GlpiLocations', on_delete=models.PROTECT)
    states = models.ForeignKey('GlpiStates', on_delete=models.PROTECT)

    class Meta:
        managed = False
        db_table = 'glpi_items_devicebatteries'


class GlpiItemsDevicecases(models.Model):
    id = models.IntegerField(primary_key=True)
    items_id = models.IntegerField()
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    devicecases = models.ForeignKey('GlpiDevicecases', on_delete=models.PROTECT)
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey('GlpiLocations', on_delete=models.PROTECT)
    states = models.ForeignKey('GlpiStates', on_delete=models.PROTECT)

    class Meta:
        managed = False
        db_table = 'glpi_items_devicecases'


class GlpiItemsDevicecontrols(models.Model):
    id = models.IntegerField(primary_key=True)
    items_id = models.IntegerField()
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    devicecontrols = models.ForeignKey('GlpiDevicecontrols', on_delete=models.PROTECT)
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    serial = models.CharField(max_length=255, blank=True, null=True)
    busid = models.CharField(db_column='busID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey('GlpiLocations', on_delete=models.PROTECT)
    states = models.ForeignKey('GlpiStates', on_delete=models.PROTECT)

    class Meta:
        managed = False
        db_table = 'glpi_items_devicecontrols'


class GlpiItemsDevicedrives(models.Model):
    id = models.IntegerField(primary_key=True)
    items_id = models.IntegerField()
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    devicedrives = models.ForeignKey('GlpiDevicedrives', on_delete=models.PROTECT)
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    serial = models.CharField(max_length=255, blank=True, null=True)
    busid = models.CharField(db_column='busID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey('GlpiLocations', on_delete=models.PROTECT)
    states = models.ForeignKey('GlpiStates', on_delete=models.PROTECT)

    class Meta:
        managed = False
        db_table = 'glpi_items_devicedrives'


class GlpiItemsDevicefirmwares(models.Model):
    id = models.IntegerField(primary_key=True)
    items_id = models.IntegerField()
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    devicefirmwares = models.ForeignKey('GlpiDevicefirmwares', on_delete=models.PROTECT)
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey('GlpiLocations', on_delete=models.PROTECT)
    states = models.ForeignKey('GlpiStates', on_delete=models.PROTECT)

    class Meta:
        managed = False
        db_table = 'glpi_items_devicefirmwares'


class GlpiItemsDevicegenerics(models.Model):
    id = models.IntegerField(primary_key=True)
    items_id = models.IntegerField()
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    devicegenerics = models.ForeignKey('GlpiDevicegenerics', on_delete=models.PROTECT)
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey('GlpiLocations', on_delete=models.PROTECT)
    states = models.ForeignKey('GlpiStates', on_delete=models.PROTECT)

    class Meta:
        managed = False
        db_table = 'glpi_items_devicegenerics'


class GlpiItemsDevicegraphiccards(models.Model):
    id = models.IntegerField(primary_key=True)
    items_id = models.IntegerField()
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    devicegraphiccards = models.ForeignKey('GlpiDevicegraphiccards', on_delete=models.PROTECT)
    memory = models.IntegerField()
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    serial = models.CharField(max_length=255, blank=True, null=True)
    busid = models.CharField(db_column='busID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey('GlpiLocations', on_delete=models.PROTECT)
    states = models.ForeignKey('GlpiStates', on_delete=models.PROTECT)

    class Meta:
        managed = False
        db_table = 'glpi_items_devicegraphiccards'


class GlpiItemsDeviceharddrives(models.Model):
    id = models.IntegerField(primary_key=True)
    items_id = models.IntegerField()
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    deviceharddrives = models.ForeignKey('GlpiDeviceharddrives', on_delete=models.PROTECT)
    capacity = models.IntegerField()
    serial = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    busid = models.CharField(db_column='busID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey('GlpiLocations', on_delete=models.PROTECT)
    states = models.ForeignKey('GlpiStates', on_delete=models.PROTECT)

    class Meta:
        managed = False
        db_table = 'glpi_items_deviceharddrives'


class GlpiItemsDevicememories(models.Model):
    id = models.IntegerField(primary_key=True)
    items_id = models.IntegerField()
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    devicememories = models.ForeignKey('GlpiDevicememories', on_delete=models.PROTECT)
    size = models.IntegerField()
    serial = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    busid = models.CharField(db_column='busID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey('GlpiLocations', on_delete=models.PROTECT)
    states = models.ForeignKey('GlpiStates', on_delete=models.PROTECT)

    class Meta:
        managed = False
        db_table = 'glpi_items_devicememories'


class GlpiItemsDevicemotherboards(models.Model):
    id = models.IntegerField(primary_key=True)
    items_id = models.IntegerField()
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    devicemotherboards = models.ForeignKey('GlpiDevicemotherboards', on_delete=models.PROTECT)
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey('GlpiLocations', on_delete=models.PROTECT)
    states = models.ForeignKey('GlpiStates', on_delete=models.PROTECT)

    class Meta:
        managed = False
        db_table = 'glpi_items_devicemotherboards'


class GlpiItemsDevicenetworkcards(models.Model):
    id = models.IntegerField(primary_key=True)
    items_id = models.IntegerField()
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    devicenetworkcards = models.ForeignKey('GlpiDevicenetworkcards', on_delete=models.PROTECT)
    mac = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    serial = models.CharField(max_length=255, blank=True, null=True)
    busid = models.CharField(db_column='busID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey('GlpiLocations', on_delete=models.PROTECT)
    states = models.ForeignKey('GlpiStates', on_delete=models.PROTECT)

    class Meta:
        managed = False
        db_table = 'glpi_items_devicenetworkcards'


class GlpiItemsDevicepcis(models.Model):
    id = models.IntegerField(primary_key=True)
    items_id = models.IntegerField()
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    devicepcis = models.ForeignKey('GlpiDevicepcis', on_delete=models.PROTECT)
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    serial = models.CharField(max_length=255, blank=True, null=True)
    busid = models.CharField(db_column='busID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey('GlpiLocations', on_delete=models.PROTECT)
    states = models.ForeignKey('GlpiStates', on_delete=models.PROTECT)

    class Meta:
        managed = False
        db_table = 'glpi_items_devicepcis'


class GlpiItemsDevicepowersupplies(models.Model):
    id = models.IntegerField(primary_key=True)
    items_id = models.IntegerField()
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    devicepowersupplies = models.ForeignKey('GlpiDevicepowersupplies', on_delete=models.PROTECT)
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey('GlpiLocations', on_delete=models.PROTECT)
    states = models.ForeignKey('GlpiStates', on_delete=models.PROTECT)

    class Meta:
        managed = False
        db_table = 'glpi_items_devicepowersupplies'


class GlpiItemsDeviceprocessors(models.Model):
    id = models.IntegerField(primary_key=True)
    items_id = models.IntegerField()
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    deviceprocessors = models.ForeignKey('GlpiDeviceprocessors', on_delete=models.PROTECT)
    frequency = models.IntegerField()
    serial = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    nbcores = models.IntegerField(blank=True, null=True)
    nbthreads = models.IntegerField(blank=True, null=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    busid = models.CharField(db_column='busID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey('GlpiLocations', on_delete=models.PROTECT)
    states = models.ForeignKey('GlpiStates', on_delete=models.PROTECT)

    class Meta:
        managed = False
        db_table = 'glpi_items_deviceprocessors'


class GlpiItemsDevicesensors(models.Model):
    id = models.IntegerField(primary_key=True)
    items_id = models.IntegerField()
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    devicesensors = models.ForeignKey('GlpiDevicesensors', on_delete=models.PROTECT)
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey('GlpiLocations', on_delete=models.PROTECT)
    states = models.ForeignKey('GlpiStates', on_delete=models.PROTECT)

    class Meta:
        managed = False
        db_table = 'glpi_items_devicesensors'


class GlpiItemsDevicesimcards(models.Model):
    id = models.IntegerField(primary_key=True)
    items_id = models.IntegerField()
    itemtype = models.CharField(max_length=100)
    devicesimcards = models.ForeignKey('GlpiDevicesimcards', on_delete=models.PROTECT)
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    states = models.ForeignKey('GlpiStates', on_delete=models.PROTECT)
    locations = models.ForeignKey('GlpiLocations', on_delete=models.PROTECT)
    lines = models.ForeignKey('GlpiLines', on_delete=models.PROTECT)
    users = models.ForeignKey('GlpiUsers', on_delete=models.PROTECT)
    groups = models.ForeignKey('GlpiGroups', on_delete=models.PROTECT)
    pin = models.CharField(max_length=255)
    pin2 = models.CharField(max_length=255)
    puk = models.CharField(max_length=255)
    puk2 = models.CharField(max_length=255)
    msin = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'glpi_items_devicesimcards'


class GlpiItemsDevicesoundcards(models.Model):
    id = models.IntegerField(primary_key=True)
    items_id = models.IntegerField()
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    devicesoundcards = models.ForeignKey('GlpiDevicesoundcards', on_delete=models.PROTECT)
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    serial = models.CharField(max_length=255, blank=True, null=True)
    busid = models.CharField(db_column='busID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey('GlpiLocations', on_delete=models.PROTECT)
    states = models.ForeignKey('GlpiStates', on_delete=models.PROTECT)

    class Meta:
        managed = False
        db_table = 'glpi_items_devicesoundcards'


class GlpiItemsDisks(models.Model):
    id = models.IntegerField(primary_key=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    items_id = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    device = models.CharField(max_length=255, blank=True, null=True)
    mountpoint = models.CharField(max_length=255, blank=True, null=True)
    filesystems = models.ForeignKey('GlpiFilesystems', on_delete=models.PROTECT)
    totalsize = models.IntegerField()
    freesize = models.IntegerField()
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    encryption_status = models.IntegerField()
    encryption_tool = models.CharField(max_length=255, blank=True, null=True)
    encryption_algorithm = models.CharField(max_length=255, blank=True, null=True)
    encryption_type = models.CharField(max_length=255, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_items_disks'


class GlpiItemsEnclosures(models.Model):
    id = models.IntegerField(primary_key=True)
    enclosures = models.ForeignKey('GlpiEnclosures', on_delete=models.PROTECT)
    itemtype = models.CharField(max_length=255)
    items_id = models.IntegerField()
    position = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_items_enclosures'
        unique_together = (('itemtype', 'items_id'),)


class GlpiItemsKanbans(models.Model):
    id = models.IntegerField(primary_key=True)
    itemtype = models.CharField(max_length=100)
    items_id = models.IntegerField(blank=True, null=True)
    users = models.ForeignKey('GlpiUsers', on_delete=models.PROTECT)
    state = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_items_kanbans'
        unique_together = ('itemtype', 'items_id', 'users')


class GlpiItemsOperatingsystems(models.Model):
    id = models.IntegerField(primary_key=True)
    items_id = models.IntegerField()
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    operatingsystems = models.ForeignKey('GlpiOperatingsystems', on_delete=models.PROTECT)
    operatingsystemversions = models.ForeignKey('GlpiOperatingsystemversions', on_delete=models.PROTECT)
    operatingsystemservicepacks = models.ForeignKey('GlpiOperatingsystemservicepacks', on_delete=models.PROTECT)
    operatingsystemarchitectures = models.ForeignKey('GlpiOperatingsystemarchitectures', on_delete=models.PROTECT)
    operatingsystemkernelversions = models.ForeignKey('GlpiOperatingsystemkernelversions', on_delete=models.PROTECT)
    license_number = models.CharField(max_length=255, blank=True, null=True)
    licenseid = models.CharField(max_length=255, blank=True, null=True)
    operatingsystemeditions_id = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_items_operatingsystems'
        unique_together = ('items_id', 'itemtype', 'operatingsystems', 'operatingsystemarchitectures')


class GlpiItemsProblems(models.Model):
    id = models.IntegerField(primary_key=True)
    problems = models.ForeignKey('GlpiProblems', on_delete=models.PROTECT)
    itemtype = models.CharField(max_length=100, blank=True, null=True)
    items_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_items_problems'
        unique_together = ('problems', 'itemtype', 'items_id')


class GlpiItemsProjects(models.Model):
    id = models.IntegerField(primary_key=True)
    projects = models.ForeignKey('GlpiProjects', on_delete=models.PROTECT)
    itemtype = models.CharField(max_length=100, blank=True, null=True)
    items_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_items_projects'
        unique_together = ('projects', 'itemtype', 'items_id')


class GlpiItemsRacks(models.Model):
    id = models.IntegerField(primary_key=True)
    racks = models.ForeignKey('GlpiRacks', on_delete=models.PROTECT)
    itemtype = models.CharField(max_length=255)
    items_id = models.IntegerField()
    position = models.IntegerField()
    orientation = models.IntegerField(blank=True, null=True)
    bgcolor = models.CharField(max_length=7, blank=True, null=True)
    hpos = models.IntegerField()
    is_reserved = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_items_racks'
        unique_together = ('itemtype', 'items_id', 'is_reserved')


class GlpiItemsSoftwarelicenses(models.Model):
    id = models.IntegerField(primary_key=True)
    items_id = models.IntegerField()
    itemtype = models.CharField(max_length=100)
    softwarelicenses = models.ForeignKey('GlpiSoftwarelicenses', on_delete=models.PROTECT)
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_items_softwarelicenses'


class GlpiItemsSoftwareversions(models.Model):
    id = models.IntegerField(primary_key=True)
    items_id = models.IntegerField()
    itemtype = models.CharField(max_length=100)
    softwareversions = models.ForeignKey('GlpiSoftwareversions', on_delete=models.PROTECT)
    is_deleted_item = models.IntegerField()
    is_template_item = models.IntegerField()
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    date_install = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_items_softwareversions'
        unique_together = ('itemtype', 'items_id', 'softwareversions')


class GlpiItemsTickets(models.Model):
    id = models.IntegerField(primary_key=True)
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    items_id = models.IntegerField()
    tickets = models.ForeignKey('GlpiTickets', on_delete=models.PROTECT)

    class Meta:
        managed = False
        db_table = 'glpi_items_tickets'
        unique_together = ('itemtype', 'items_id', 'tickets')


class GlpiItilcategories(models.Model):
    id = models.IntegerField(primary_key=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    itilcategories = models.ForeignKey('GlpiItilcategories', on_delete=models.PROTECT)
    name = models.CharField(max_length=255, blank=True, null=True)
    completename = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    level = models.IntegerField()
    knowbaseitemcategories = models.ForeignKey('GlpiKnowbaseitemcategories', on_delete=models.PROTECT)
    users = models.ForeignKey('GlpiUsers', on_delete=models.PROTECT)
    groups = models.ForeignKey('GlpiGroups', on_delete=models.PROTECT)
    code = models.CharField(max_length=255, blank=True, null=True)
    ancestors_cache = models.TextField(blank=True, null=True)
    sons_cache = models.TextField(blank=True, null=True)
    is_helpdeskvisible = models.IntegerField()
    tickettemplates_id_incident = models.IntegerField()
    tickettemplates_id_demand = models.IntegerField()
    changetemplates = models.ForeignKey('GlpiChangetemplates', on_delete=models.PROTECT)
    problemtemplates = models.ForeignKey('GlpiProblemtemplates', on_delete=models.PROTECT)
    is_incident = models.IntegerField()
    is_request = models.IntegerField()
    is_problem = models.IntegerField()
    is_change = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_itilcategories'


class GlpiItilfollowups(models.Model):
    id = models.IntegerField(primary_key=True)
    itemtype = models.CharField(max_length=100)
    items_id = models.IntegerField()
    date = models.DateTimeField(blank=True, null=True)
    users = models.ForeignKey('GlpiUsers', on_delete=models.PROTECT)
    users_id_editor = models.IntegerField()
    content = models.TextField(blank=True, null=True)
    is_private = models.IntegerField()
    requesttypes = models.ForeignKey('GlpiRequesttypes', on_delete=models.PROTECT)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    timeline_position = models.IntegerField()
    sourceitems_id = models.IntegerField()
    sourceof_items_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_itilfollowups'


class GlpiItilfollowuptemplates(models.Model):
    id = models.IntegerField(primary_key=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    requesttypes = models.ForeignKey('GlpiRequesttypes', on_delete=models.PROTECT)
    is_private = models.IntegerField()
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_itilfollowuptemplates'


class GlpiItilsProjects(models.Model):
    id = models.IntegerField(primary_key=True)
    itemtype = models.CharField(max_length=100)
    items_id = models.IntegerField()
    projects = models.ForeignKey('GlpiProjects', on_delete=models.PROTECT)

    class Meta:
        managed = False
        db_table = 'glpi_itils_projects'
        unique_together = ('itemtype', 'items_id', 'projects')


class GlpiItilsolutions(models.Model):
    id = models.IntegerField(primary_key=True)
    itemtype = models.CharField(max_length=100)
    items_id = models.IntegerField()
    solutiontypes = models.ForeignKey('GlpiSolutiontypes', on_delete=models.PROTECT)
    solutiontype_name = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_approval = models.DateTimeField(blank=True, null=True)
    users = models.ForeignKey('GlpiUsers', on_delete=models.PROTECT)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    users_id_editor = models.IntegerField()
    users_id_approval = models.IntegerField()
    user_name_approval = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField()
    itilfollowups = models.ForeignKey('GlpiItilfollowups', on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_itilsolutions'


class GlpiKnowbaseitemcategories(models.Model):
    id = models.IntegerField(primary_key=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    knowbaseitemcategories = models.ForeignKey('GlpiKnowbaseitemcategories', on_delete=models.PROTECT)
    name = models.CharField(max_length=255, blank=True, null=True)
    completename = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    level = models.IntegerField()
    sons_cache = models.TextField(blank=True, null=True)
    ancestors_cache = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_knowbaseitemcategories'
        unique_together = ('entities', 'knowbaseitemcategories', 'name')


class GlpiKnowbaseitems(models.Model):
    id = models.IntegerField(primary_key=True)
    knowbaseitemcategories = models.ForeignKey('GlpiKnowbaseitemcategories', on_delete=models.PROTECT)
    name = models.TextField(blank=True, null=True)
    answer = models.TextField(blank=True, null=True)
    is_faq = models.IntegerField()
    users = models.ForeignKey('GlpiUsers', on_delete=models.PROTECT)
    view = models.IntegerField()
    date = models.DateTimeField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    begin_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_knowbaseitems'


class GlpiKnowbaseitemsComments(models.Model):
    id = models.IntegerField(primary_key=True)
    knowbaseitems = models.ForeignKey('GlpiKnowbaseitems', on_delete=models.PROTECT)
    users = models.ForeignKey('GlpiUsers', on_delete=models.PROTECT)
    language = models.CharField(max_length=10, blank=True, null=True)
    comment = models.TextField()
    parent_comment_id = models.IntegerField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_knowbaseitems_comments'


class GlpiKnowbaseitemsItems(models.Model):
    id = models.IntegerField(primary_key=True)
    knowbaseitems = models.ForeignKey('GlpiKnowbaseitems', on_delete=models.PROTECT)
    itemtype = models.CharField(max_length=100)
    items_id = models.IntegerField()
    date_creation = models.DateTimeField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_knowbaseitems_items'
        unique_together = ('itemtype', 'items_id', 'knowbaseitems')


class GlpiKnowbaseitemsProfiles(models.Model):
    id = models.IntegerField(primary_key=True)
    knowbaseitems = models.ForeignKey('GlpiKnowbaseitems', on_delete=models.PROTECT)
    profiles = models.ForeignKey('GlpiProfiles', on_delete=models.PROTECT)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_knowbaseitems_profiles'


class GlpiKnowbaseitemsRevisions(models.Model):
    id = models.IntegerField(primary_key=True)
    knowbaseitems = models.ForeignKey('GlpiKnowbaseitems', on_delete=models.PROTECT)
    revision = models.IntegerField()
    name = models.TextField(blank=True, null=True)
    answer = models.TextField(blank=True, null=True)
    language = models.CharField(max_length=10, blank=True, null=True)
    users = models.ForeignKey('GlpiUsers', on_delete=models.PROTECT)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_knowbaseitems_revisions'
        unique_together = ('knowbaseitems', 'revision', 'language')


class GlpiKnowbaseitemsUsers(models.Model):
    id = models.IntegerField(primary_key=True)
    knowbaseitems = models.ForeignKey('GlpiKnowbaseitems', on_delete=models.PROTECT)
    users = models.ForeignKey('GlpiUsers', on_delete=models.PROTECT)

    class Meta:
        managed = False
        db_table = 'glpi_knowbaseitems_users'


class GlpiKnowbaseitemtranslations(models.Model):
    id = models.IntegerField(primary_key=True)
    knowbaseitems = models.ForeignKey('GlpiKnowbaseitems', on_delete=models.PROTECT)
    language = models.CharField(max_length=10, blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    answer = models.TextField(blank=True, null=True)
    users = models.ForeignKey('GlpiUsers', on_delete=models.PROTECT)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_knowbaseitemtranslations'


class GlpiLineoperators(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    comment = models.TextField(blank=True, null=True)
    mcc = models.IntegerField(blank=True, null=True)
    mnc = models.IntegerField(blank=True, null=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_lineoperators'
        unique_together = (('mcc', 'mnc'),)


class GlpiLines(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    is_deleted = models.IntegerField()
    caller_num = models.CharField(max_length=255)
    caller_name = models.CharField(max_length=255)
    users = models.ForeignKey('GlpiUsers', on_delete=models.PROTECT)
    groups = models.ForeignKey('GlpiGroups', on_delete=models.PROTECT)
    lineoperators = models.ForeignKey('GlpiLineoperators', on_delete=models.PROTECT)
    locations = models.ForeignKey('GlpiLocations', on_delete=models.PROTECT)
    states = models.ForeignKey('GlpiStates', on_delete=models.PROTECT)
    linetypes = models.ForeignKey('GlpiLinetypes', on_delete=models.PROTECT)
    date_creation = models.DateTimeField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_lines'


class GlpiLinetypes(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_linetypes'


class GlpiLinks(models.Model):
    id = models.IntegerField(primary_key=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    open_window = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_links'


class GlpiLinksItemtypes(models.Model):
    id = models.IntegerField(primary_key=True)
    links = models.ForeignKey('GlpiLinks', on_delete=models.PROTECT)
    itemtype = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'glpi_links_itemtypes'
        unique_together = ('itemtype', 'links')


class GlpiLocations(models.Model):
    id = models.IntegerField(primary_key=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey('GlpiLocations', on_delete=models.PROTECT)
    completename = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    level = models.IntegerField()
    ancestors_cache = models.TextField(blank=True, null=True)
    sons_cache = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    postcode = models.CharField(max_length=255, blank=True, null=True)
    town = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    building = models.CharField(max_length=255, blank=True, null=True)
    room = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.CharField(max_length=255, blank=True, null=True)
    longitude = models.CharField(max_length=255, blank=True, null=True)
    altitude = models.CharField(max_length=255, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_locations'
        unique_together = ('entities', 'locations', 'name')


class GlpiLogs(models.Model):
    id = models.IntegerField(primary_key=True)
    itemtype = models.CharField(max_length=100)
    items_id = models.IntegerField()
    itemtype_link = models.CharField(max_length=100)
    linked_action = models.IntegerField()
    user_name = models.CharField(max_length=255, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    id_search_option = models.IntegerField()
    old_value = models.CharField(max_length=255, blank=True, null=True)
    new_value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_logs'


class GlpiMailcollectors(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    host = models.CharField(max_length=255, blank=True, null=True)
    login = models.CharField(max_length=255, blank=True, null=True)
    filesize_max = models.IntegerField()
    is_active = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    passwd = models.CharField(max_length=255, blank=True, null=True)
    accepted = models.CharField(max_length=255, blank=True, null=True)
    refused = models.CharField(max_length=255, blank=True, null=True)
    errors = models.IntegerField()
    use_mail_date = models.IntegerField()
    date_creation = models.DateTimeField(blank=True, null=True)
    requester_field = models.IntegerField()
    add_cc_to_observer = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_mailcollectors'


class GlpiManufacturers(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_manufacturers'


class GlpiMonitormodels(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)
    weight = models.IntegerField()
    required_units = models.IntegerField()
    depth = models.FloatField()
    power_connections = models.IntegerField()
    power_consumption = models.IntegerField()
    is_half_rack = models.IntegerField()
    picture_front = models.TextField(blank=True, null=True)
    picture_rear = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_monitormodels'


class GlpiMonitors(models.Model):
    id = models.IntegerField(primary_key=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    name = models.CharField(max_length=255, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    contact = models.CharField(max_length=255, blank=True, null=True)
    contact_num = models.CharField(max_length=255, blank=True, null=True)
    users_id_tech = models.IntegerField()
    groups_id_tech = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    size = models.DecimalField(max_digits=5, decimal_places=2)
    have_micro = models.IntegerField()
    have_speaker = models.IntegerField()
    have_subd = models.IntegerField()
    have_bnc = models.IntegerField()
    have_dvi = models.IntegerField()
    have_pivot = models.IntegerField()
    have_hdmi = models.IntegerField()
    have_displayport = models.IntegerField()
    locations = models.ForeignKey('GlpiLocations', on_delete=models.PROTECT)
    monitortypes = models.ForeignKey('GlpiMonitortypes', on_delete=models.PROTECT)
    monitormodels = models.ForeignKey('GlpiMonitormodels', on_delete=models.PROTECT)
    manufacturers = models.ForeignKey('GlpiManufacturers', on_delete=models.PROTECT)
    is_global = models.IntegerField()
    is_deleted = models.IntegerField()
    is_template = models.IntegerField()
    template_name = models.CharField(max_length=255, blank=True, null=True)
    users = models.ForeignKey('GlpiUsers', on_delete=models.PROTECT)
    groups = models.ForeignKey('GlpiGroups', on_delete=models.PROTECT)
    states = models.ForeignKey('GlpiStates', on_delete=models.PROTECT)
    ticket_tco = models.DecimalField(max_digits=20, decimal_places=4, blank=True, null=True)
    is_dynamic = models.IntegerField()
    date_creation = models.DateTimeField(blank=True, null=True)
    is_recursive = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_monitors'


class GlpiMonitortypes(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_monitortypes'


class GlpiNetpoints(models.Model):
    id = models.IntegerField(primary_key=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    locations = models.ForeignKey('GlpiLocations', on_delete=models.PROTECT)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_netpoints'


class GlpiNetworkaliases(models.Model):
    id = models.IntegerField(primary_key=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    networknames = models.ForeignKey('GlpiNetworknames', on_delete=models.PROTECT)
    name = models.CharField(max_length=255, blank=True, null=True)
    fqdns = models.ForeignKey('GlpiFqdns', on_delete=models.PROTECT)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_networkaliases'


class GlpiNetworkequipmentmodels(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)
    weight = models.IntegerField()
    required_units = models.IntegerField()
    depth = models.FloatField()
    power_connections = models.IntegerField()
    power_consumption = models.IntegerField()
    is_half_rack = models.IntegerField()
    picture_front = models.TextField(blank=True, null=True)
    picture_rear = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_networkequipmentmodels'


class GlpiNetworkequipments(models.Model):
    id = models.IntegerField(primary_key=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    ram = models.CharField(max_length=255, blank=True, null=True)
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    contact = models.CharField(max_length=255, blank=True, null=True)
    contact_num = models.CharField(max_length=255, blank=True, null=True)
    users_id_tech = models.IntegerField()
    groups_id_tech = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    locations = models.ForeignKey('GlpiLocations', on_delete=models.PROTECT)
    networks = models.ForeignKey('GlpiNetworks', on_delete=models.PROTECT)
    networkequipmenttypes = models.ForeignKey('GlpiNetworkequipmenttypes', on_delete=models.PROTECT)
    networkequipmentmodels = models.ForeignKey('GlpiNetworkequipmentmodels', on_delete=models.PROTECT)
    manufacturers = models.ForeignKey('GlpiManufacturers', on_delete=models.PROTECT)
    is_deleted = models.IntegerField()
    is_template = models.IntegerField()
    template_name = models.CharField(max_length=255, blank=True, null=True)
    users = models.ForeignKey('GlpiUsers', on_delete=models.PROTECT)
    groups = models.ForeignKey('GlpiGroups', on_delete=models.PROTECT)
    states = models.ForeignKey('GlpiStates', on_delete=models.PROTECT)
    ticket_tco = models.DecimalField(max_digits=20, decimal_places=4, blank=True, null=True)
    is_dynamic = models.IntegerField()
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_networkequipments'


class GlpiNetworkequipmenttypes(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_networkequipmenttypes'


class GlpiNetworkinterfaces(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_networkinterfaces'


class GlpiNetworknames(models.Model):
    id = models.IntegerField(primary_key=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    items_id = models.IntegerField()
    itemtype = models.CharField(max_length=100)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    fqdns = models.ForeignKey('GlpiFqdns', on_delete=models.PROTECT)
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_networknames'


class GlpiNetworkportaggregates(models.Model):
    id = models.IntegerField(primary_key=True)
    networkports = models.OneToOneField('GlpiNetworkports', on_delete=models.PROTECT)
    networkports_id_list = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_networkportaggregates'


class GlpiNetworkportaliases(models.Model):
    id = models.IntegerField(primary_key=True)
    networkports = models.OneToOneField('GlpiNetworkports', on_delete=models.PROTECT)
    networkports_id_alias = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_networkportaliases'


class GlpiNetworkportdialups(models.Model):
    id = models.IntegerField(primary_key=True)
    networkports = models.OneToOneField('GlpiNetworkports', on_delete=models.PROTECT)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_networkportdialups'


class GlpiNetworkportethernets(models.Model):
    id = models.IntegerField(primary_key=True)
    networkports = models.OneToOneField('GlpiNetworkports', on_delete=models.PROTECT)
    items_devicenetworkcards = models.ForeignKey('GlpiDevicenetworkcards', on_delete=models.PROTECT)
    netpoints_id = models.IntegerField()
    type = models.CharField(max_length=10, blank=True, null=True)
    speed = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_networkportethernets'


class GlpiNetworkportfiberchannels(models.Model):
    id = models.IntegerField(primary_key=True)
    networkports = models.OneToOneField('GlpiNetworkports', on_delete=models.PROTECT)
    items_devicenetworkcards = models.ForeignKey('GlpiDevicenetworkcards', on_delete=models.PROTECT)
    netpoints_id = models.IntegerField()
    wwn = models.CharField(max_length=16, blank=True, null=True)
    speed = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_networkportfiberchannels'


class GlpiNetworkportlocals(models.Model):
    id = models.IntegerField(primary_key=True)
    networkports = models.OneToOneField('GlpiNetworkports', on_delete=models.PROTECT)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_networkportlocals'


class GlpiNetworkports(models.Model):
    id = models.IntegerField(primary_key=True)
    items_id = models.IntegerField()
    itemtype = models.CharField(max_length=100)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    logical_number = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    instantiation_type = models.CharField(max_length=255, blank=True, null=True)
    mac = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    is_deleted = models.IntegerField()
    is_dynamic = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_networkports'


class GlpiNetworkportsNetworkports(models.Model):
    id = models.IntegerField(primary_key=True)
    networkports_id_1 = models.IntegerField()
    networkports_id_2 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_networkports_networkports'
        unique_together = ('networkports_id_1', 'networkports_id_2')


class GlpiNetworkportsVlans(models.Model):
    id = models.IntegerField(primary_key=True)
    networkports = models.ForeignKey('GlpiNetworkports', on_delete=models.PROTECT)
    vlans = models.ForeignKey('GlpiVlans', on_delete=models.PROTECT)
    tagged = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_networkports_vlans'
        unique_together = ('networkports', 'vlans')


class GlpiNetworkportwifis(models.Model):
    id = models.IntegerField(primary_key=True)
    networkports = models.OneToOneField('GlpiNetworkports', on_delete=models.PROTECT)
    items_devicenetworkcards = models.ForeignKey('GlpiDevicenetworkcards', on_delete=models.PROTECT)
    wifinetworks = models.ForeignKey('GlpiWifinetworks', on_delete=models.PROTECT)
    networkportwifis = models.ForeignKey('self', on_delete=models.PROTECT)
    version = models.CharField(max_length=20, blank=True, null=True)
    mode = models.CharField(max_length=20, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_networkportwifis'


class GlpiNetworks(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_networks'


class GlpiNotepads(models.Model):
    id = models.IntegerField(primary_key=True)
    itemtype = models.CharField(max_length=100, blank=True, null=True)
    items_id = models.IntegerField()
    date = models.DateTimeField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    users = models.ForeignKey('GlpiUsers', on_delete=models.PROTECT)
    users_id_lastupdater = models.IntegerField()
    content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_notepads'


class GlpiNotifications(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    itemtype = models.CharField(max_length=100)
    event = models.CharField(max_length=255)
    comment = models.TextField(blank=True, null=True)
    is_recursive = models.IntegerField()
    is_active = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    allow_response = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_notifications'


class GlpiNotificationsNotificationtemplates(models.Model):
    id = models.IntegerField(primary_key=True)
    notifications = models.ForeignKey('GlpiNotifications', on_delete=models.PROTECT)
    mode = models.CharField(max_length=20)
    notificationtemplates = models.ForeignKey('GlpiNotificationtemplates', on_delete=models.PROTECT)

    class Meta:
        managed = False
        db_table = 'glpi_notifications_notificationtemplates'
        unique_together = ('notifications', 'mode', 'notificationtemplates')


class GlpiNotificationtargets(models.Model):
    id = models.IntegerField(primary_key=True)
    items_id = models.IntegerField()
    type = models.IntegerField()
    notifications = models.ForeignKey('GlpiNotifications', on_delete=models.PROTECT)

    class Meta:
        managed = False
        db_table = 'glpi_notificationtargets'


class GlpiNotificationtemplates(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    itemtype = models.CharField(max_length=100)
    date_mod = models.DateTimeField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    css = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_notificationtemplates'


class GlpiNotificationtemplatetranslations(models.Model):
    id = models.IntegerField(primary_key=True)
    notificationtemplates = models.ForeignKey('GlpiNotificationtemplates', on_delete=models.PROTECT)
    language = models.CharField(max_length=10)
    subject = models.CharField(max_length=255)
    content_text = models.TextField(blank=True, null=True)
    content_html = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_notificationtemplatetranslations'


class GlpiNotimportedemails(models.Model):
    id = models.IntegerField(primary_key=True)
    from_field = models.CharField(db_column='from', max_length=255)  # Field renamed because it was a Python reserved word.
    to = models.CharField(max_length=255)
    mailcollectors = models.ForeignKey('GlpiMailcollectors', on_delete=models.PROTECT)
    date = models.DateTimeField()
    subject = models.TextField(blank=True, null=True)
    messageid = models.CharField(max_length=255)
    reason = models.IntegerField()
    users = models.ForeignKey('GlpiUsers', on_delete=models.PROTECT)

    class Meta:
        managed = False
        db_table = 'glpi_notimportedemails'


class GlpiObjectlocks(models.Model):
    id = models.IntegerField(primary_key=True)
    itemtype = models.CharField(max_length=100)
    items_id = models.IntegerField()
    users = models.ForeignKey('GlpiUsers', on_delete=models.PROTECT)
    date_mod = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'glpi_objectlocks'
        unique_together = ('itemtype', 'items_id')


class GlpiOlalevelactions(models.Model):
    id = models.IntegerField(primary_key=True)
    olalevels = models.ForeignKey('GlpiOlalevels', on_delete=models.PROTECT)
    action_type = models.CharField(max_length=255, blank=True, null=True)
    field = models.CharField(max_length=255, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_olalevelactions'


class GlpiOlalevelcriterias(models.Model):
    id = models.IntegerField(primary_key=True)
    olalevels = models.ForeignKey('GlpiOlalevels', on_delete=models.PROTECT)
    criteria = models.CharField(max_length=255, blank=True, null=True)
    condition = models.IntegerField()
    pattern = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_olalevelcriterias'


class GlpiOlalevels(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    olas = models.ForeignKey('GlpiOlas', on_delete=models.PROTECT)
    execution_time = models.IntegerField()
    is_active = models.IntegerField()
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    match = models.CharField(max_length=10, blank=True, null=True)
    uuid = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_olalevels'


class GlpiOlalevelsTickets(models.Model):
    id = models.IntegerField(primary_key=True)
    tickets = models.ForeignKey('GlpiTickets', on_delete=models.PROTECT)
    olalevels = models.ForeignKey('GlpiOlalevels', on_delete=models.PROTECT)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_olalevels_tickets'
        unique_together = ('tickets', 'olalevels')


class GlpiOlas(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    type = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    number_time = models.IntegerField()
    calendars = models.ForeignKey('GlpiCalendars', on_delete=models.PROTECT)
    date_mod = models.DateTimeField(blank=True, null=True)
    definition_time = models.CharField(max_length=255, blank=True, null=True)
    end_of_working_day = models.IntegerField()
    date_creation = models.DateTimeField(blank=True, null=True)
    slms = models.ForeignKey('GlpiSlms', on_delete=models.PROTECT)

    class Meta:
        managed = False
        db_table = 'glpi_olas'


class GlpiOperatingsystemarchitectures(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_operatingsystemarchitectures'


class GlpiOperatingsystemeditions(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_operatingsystemeditions'


class GlpiOperatingsystemkernels(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_operatingsystemkernels'


class GlpiOperatingsystemkernelversions(models.Model):
    id = models.IntegerField(primary_key=True)
    operatingsystemkernels = models.ForeignKey('GlpiOperatingsystemkernels', on_delete=models.PROTECT)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_operatingsystemkernelversions'


class GlpiOperatingsystems(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_operatingsystems'


class GlpiOperatingsystemservicepacks(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_operatingsystemservicepacks'


class GlpiOperatingsystemversions(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_operatingsystemversions'


class GlpiPassivedcequipmentmodels(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)
    weight = models.IntegerField()
    required_units = models.IntegerField()
    depth = models.FloatField()
    power_connections = models.IntegerField()
    power_consumption = models.IntegerField()
    is_half_rack = models.IntegerField()
    picture_front = models.TextField(blank=True, null=True)
    picture_rear = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_passivedcequipmentmodels'


class GlpiPassivedcequipments(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    locations = models.ForeignKey('GlpiLocations', on_delete=models.PROTECT)
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    passivedcequipmentmodels = models.ForeignKey('GlpiPassivedcequipmentmodels', on_delete=models.SET_NULL, blank=True, null=True)
    passivedcequipmenttypes = models.ForeignKey('GlpiPassivedcequipmenttypes', on_delete=models.PROTECT)
    users_id_tech = models.IntegerField()
    groups_id_tech = models.IntegerField()
    is_template = models.IntegerField()
    template_name = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.IntegerField()
    states = models.ForeignKey('GlpiStates', on_delete=models.PROTECT)
    comment = models.TextField(blank=True, null=True)
    manufacturers = models.ForeignKey('GlpiManufacturers', on_delete=models.PROTECT)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_passivedcequipments'


class GlpiPassivedcequipmenttypes(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_passivedcequipmenttypes'


class GlpiPdumodels(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)
    weight = models.IntegerField()
    required_units = models.IntegerField()
    depth = models.FloatField()
    power_connections = models.IntegerField()
    max_power = models.IntegerField()
    is_half_rack = models.IntegerField()
    picture_front = models.TextField(blank=True, null=True)
    picture_rear = models.TextField(blank=True, null=True)
    is_rackable = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_pdumodels'


class GlpiPdus(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    locations = models.ForeignKey('GlpiLocations', on_delete=models.PROTECT)
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    pdumodels = models.ForeignKey('GlpiPdumodels', on_delete=models.SET_NULL, blank=True, null=True)
    users_id_tech = models.IntegerField()
    groups_id_tech = models.IntegerField()
    is_template = models.IntegerField()
    template_name = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.IntegerField()
    states = models.ForeignKey('GlpiStates', on_delete=models.PROTECT)
    comment = models.TextField(blank=True, null=True)
    manufacturers = models.ForeignKey('GlpiManufacturers', on_delete=models.PROTECT)
    pdutypes = models.ForeignKey('GlpiPdutypes', on_delete=models.PROTECT)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_pdus'


class GlpiPdusPlugs(models.Model):
    id = models.IntegerField(primary_key=True)
    plugs = models.ForeignKey('GlpiPlugs', on_delete=models.PROTECT)
    pdus = models.ForeignKey('GlpiPdus', on_delete=models.PROTECT)
    number_plugs = models.IntegerField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_pdus_plugs'


class GlpiPdusRacks(models.Model):
    id = models.IntegerField(primary_key=True)
    racks = models.ForeignKey('GlpiRacks', on_delete=models.PROTECT)
    pdus = models.ForeignKey('GlpiPdus', on_delete=models.PROTECT)
    side = models.IntegerField(blank=True, null=True)
    position = models.IntegerField()
    bgcolor = models.CharField(max_length=7, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_pdus_racks'


class GlpiPdutypes(models.Model):
    id = models.IntegerField(primary_key=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_pdutypes'


class GlpiPeripheralmodels(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)
    weight = models.IntegerField()
    required_units = models.IntegerField()
    depth = models.FloatField()
    power_connections = models.IntegerField()
    power_consumption = models.IntegerField()
    is_half_rack = models.IntegerField()
    picture_front = models.TextField(blank=True, null=True)
    picture_rear = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_peripheralmodels'


class GlpiPeripherals(models.Model):
    id = models.IntegerField(primary_key=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    name = models.CharField(max_length=255, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    contact = models.CharField(max_length=255, blank=True, null=True)
    contact_num = models.CharField(max_length=255, blank=True, null=True)
    users_id_tech = models.IntegerField()
    groups_id_tech = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey('GlpiLocations', on_delete=models.PROTECT)
    peripheraltypes = models.ForeignKey('GlpiPeripheraltypes', on_delete=models.PROTECT)
    peripheralmodels = models.ForeignKey('GlpiPeripheralmodels', on_delete=models.PROTECT)
    brand = models.CharField(max_length=255, blank=True, null=True)
    manufacturers = models.ForeignKey('GlpiManufacturers', on_delete=models.PROTECT)
    is_global = models.IntegerField()
    is_deleted = models.IntegerField()
    is_template = models.IntegerField()
    template_name = models.CharField(max_length=255, blank=True, null=True)
    users = models.ForeignKey('GlpiUsers', on_delete=models.PROTECT)
    groups = models.ForeignKey('GlpiGroups', on_delete=models.PROTECT)
    states = models.ForeignKey('GlpiStates', on_delete=models.PROTECT)
    ticket_tco = models.DecimalField(max_digits=20, decimal_places=4, blank=True, null=True)
    is_dynamic = models.IntegerField()
    date_creation = models.DateTimeField(blank=True, null=True)
    is_recursive = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_peripherals'


class GlpiPeripheraltypes(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_peripheraltypes'


class GlpiPhonemodels(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_phonemodels'


class GlpiPhonepowersupplies(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_phonepowersupplies'


class GlpiPhones(models.Model):
    id = models.IntegerField(primary_key=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    name = models.CharField(max_length=255, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    contact = models.CharField(max_length=255, blank=True, null=True)
    contact_num = models.CharField(max_length=255, blank=True, null=True)
    users_id_tech = models.IntegerField()
    groups_id_tech = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey('GlpiLocations', on_delete=models.PROTECT)
    phonetypes = models.ForeignKey('GlpiPhonetypes', on_delete=models.PROTECT)
    phonemodels = models.ForeignKey('GlpiPhonemodels', on_delete=models.PROTECT)
    brand = models.CharField(max_length=255, blank=True, null=True)
    phonepowersupplies = models.ForeignKey('GlpiPhonepowersupplies', on_delete=models.PROTECT)
    number_line = models.CharField(max_length=255, blank=True, null=True)
    have_headset = models.IntegerField()
    have_hp = models.IntegerField()
    manufacturers = models.ForeignKey('GlpiManufacturers', on_delete=models.PROTECT)
    is_global = models.IntegerField()
    is_deleted = models.IntegerField()
    is_template = models.IntegerField()
    template_name = models.CharField(max_length=255, blank=True, null=True)
    users = models.ForeignKey('GlpiUsers', on_delete=models.PROTECT)
    groups = models.ForeignKey('GlpiGroups', on_delete=models.PROTECT)
    states = models.ForeignKey('GlpiStates', on_delete=models.PROTECT)
    ticket_tco = models.DecimalField(max_digits=20, decimal_places=4, blank=True, null=True)
    is_dynamic = models.IntegerField()
    date_creation = models.DateTimeField(blank=True, null=True)
    is_recursive = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_phones'


class GlpiPhonetypes(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_phonetypes'


class GlpiPlanningeventcategories(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_planningeventcategories'


class GlpiPlanningexternalevents(models.Model):
    id = models.IntegerField(primary_key=True)
    uuid = models.CharField(unique=True, max_length=255, blank=True, null=True)
    planningexternaleventtemplates = models.ForeignKey('GlpiPlanningexternaleventtemplates', on_delete=models.PROTECT)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    date = models.DateTimeField(blank=True, null=True)
    users = models.ForeignKey('GlpiUsers', on_delete=models.PROTECT)
    users_id_guests = models.TextField(blank=True, null=True)
    groups = models.ForeignKey('GlpiGroups', on_delete=models.PROTECT)
    name = models.CharField(max_length=255, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    begin = models.DateTimeField(blank=True, null=True)
    end = models.DateTimeField(blank=True, null=True)
    rrule = models.TextField(blank=True, null=True)
    state = models.IntegerField()
    planningeventcategories = models.ForeignKey('GlpiPlanningeventcategories', on_delete=models.PROTECT)
    background = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_planningexternalevents'


class GlpiPlanningexternaleventtemplates(models.Model):
    id = models.IntegerField(primary_key=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    name = models.CharField(max_length=255, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    duration = models.IntegerField()
    before_time = models.IntegerField()
    rrule = models.TextField(blank=True, null=True)
    state = models.IntegerField()
    planningeventcategories = models.ForeignKey('GlpiPlanningeventcategories', on_delete=models.PROTECT)
    background = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_planningexternaleventtemplates'


class GlpiPlanningrecalls(models.Model):
    id = models.IntegerField(primary_key=True)
    items_id = models.IntegerField()
    itemtype = models.CharField(max_length=100)
    users = models.ForeignKey('GlpiUsers', on_delete=models.PROTECT)
    before_time = models.IntegerField()
    when = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_planningrecalls'
        unique_together = ('itemtype', 'items_id', 'users')


class GlpiPluginDatainjectionInfos(models.Model):
    id = models.IntegerField(primary_key=True)
    models_id = models.IntegerField()
    itemtype = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    is_mandatory = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_plugin_datainjection_infos'


class GlpiPluginDatainjectionMappings(models.Model):
    id = models.IntegerField(primary_key=True)
    models_id = models.IntegerField()
    itemtype = models.CharField(max_length=255)
    rank = models.IntegerField()
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    is_mandatory = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_plugin_datainjection_mappings'


class GlpiPluginDatainjectionModelcsvs(models.Model):
    id = models.IntegerField(primary_key=True)
    models_id = models.IntegerField()
    itemtype = models.CharField(max_length=255)
    delimiter = models.CharField(max_length=1)
    is_header_present = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_plugin_datainjection_modelcsvs'


class GlpiPluginDatainjectionModels(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    filetype = models.CharField(max_length=255)
    itemtype = models.CharField(max_length=255)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    behavior_add = models.IntegerField()
    behavior_update = models.IntegerField()
    can_add_dropdown = models.IntegerField()
    can_overwrite_if_not_empty = models.IntegerField()
    is_private = models.IntegerField()
    is_recursive = models.IntegerField()
    perform_network_connection = models.IntegerField()
    users = models.ForeignKey('GlpiUsers', on_delete=models.PROTECT)
    date_format = models.CharField(max_length=11)
    float_format = models.IntegerField()
    port_unicity = models.IntegerField()
    step = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_plugin_datainjection_models'


class GlpiPluginFieldsContainers(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    label = models.CharField(max_length=255, blank=True, null=True)
    itemtypes = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    subtype = models.CharField(max_length=255, blank=True, null=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    is_active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_plugin_fields_containers'


class GlpiPluginFieldsFields(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    label = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=25, blank=True, null=True)
    plugin_fields_containers = models.ForeignKey('GlpiPluginFieldsContainers', on_delete=models.PROTECT)
    ranking = models.IntegerField()
    default_value = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.IntegerField()
    is_readonly = models.IntegerField()
    mandatory = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_plugin_fields_fields'


class GlpiPluginFieldsLabeltranslations(models.Model):
    id = models.IntegerField(primary_key=True)
    plugin_fields_itemtype = models.CharField(max_length=30)
    plugin_fields_items_id = models.IntegerField()
    language = models.CharField(max_length=5)
    label = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_plugin_fields_labeltranslations'
        unique_together = (('plugin_fields_itemtype', 'plugin_fields_items_id', 'language'),)


class GlpiPluginFieldsProfiles(models.Model):
    id = models.IntegerField(primary_key=True)
    profiles = models.ForeignKey('GlpiProfiles', on_delete=models.PROTECT)
    plugin_fields_containers = models.ForeignKey('GlpiPluginFieldsContainers', on_delete=models.PROTECT)
    right = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_plugin_fields_profiles'


class GlpiPluginFormcreatorAnswers(models.Model):
    id = models.IntegerField(primary_key=True)
    plugin_formcreator_formanswers_id = models.IntegerField()
    plugin_formcreator_questions = models.ForeignKey('GlpiPluginFormcreatorQuestions', on_delete=models.PROTECT)
    answer = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_plugin_formcreator_answers'


class GlpiPluginFormcreatorCategories(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    comment = models.TextField(blank=True, null=True)
    completename = models.CharField(max_length=255, blank=True, null=True)
    plugin_formcreator_categories = models.ForeignKey('self', on_delete=models.PROTECT)
    level = models.IntegerField()
    sons_cache = models.TextField(blank=True, null=True)
    ancestors_cache = models.TextField(blank=True, null=True)
    knowbaseitemcategories = models.ForeignKey('GlpiKnowbaseitemcategories', on_delete=models.PROTECT)

    class Meta:
        managed = False
        db_table = 'glpi_plugin_formcreator_categories'


class GlpiPluginFormcreatorConditions(models.Model):
    id = models.IntegerField(primary_key=True)
    itemtype = models.CharField(max_length=255)
    items_id = models.IntegerField()
    plugin_formcreator_questions = models.ForeignKey('GlpiPluginFormcreatorQuestions', on_delete=models.PROTECT)
    show_condition = models.IntegerField()
    show_value = models.CharField(max_length=255, blank=True, null=True)
    show_logic = models.IntegerField()
    order = models.IntegerField()
    uuid = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_plugin_formcreator_conditions'


class GlpiPluginFormcreatorEntityconfigs(models.Model):
    id = models.IntegerField(primary_key=True)
    replace_helpdesk = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_plugin_formcreator_entityconfigs'


class GlpiPluginFormcreatorFormanswers(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    plugin_formcreator_forms = models.ForeignKey('GlpiPluginFormcreatorForms', on_delete=models.PROTECT)
    requester_id = models.IntegerField(blank=True, null=True)
    users_id_validator = models.IntegerField()
    groups_id_validator = models.IntegerField()
    request_date = models.DateTimeField()
    status = models.IntegerField()
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_plugin_formcreator_formanswers'


class GlpiPluginFormcreatorForms(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    icon = models.CharField(max_length=255)
    icon_color = models.CharField(max_length=255)
    background_color = models.CharField(max_length=255)
    access_rights = models.IntegerField()
    requesttype = models.IntegerField()
    description = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    plugin_formcreator_categories = models.ForeignKey('GlpiPluginFormcreatorCategories', on_delete=models.PROTECT)
    is_active = models.IntegerField()
    language = models.CharField(max_length=5)
    helpdesk_home = models.IntegerField()
    is_deleted = models.IntegerField()
    validation_required = models.IntegerField()
    usage_count = models.IntegerField()
    is_default = models.IntegerField()
    show_rule = models.IntegerField()
    uuid = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_plugin_formcreator_forms'


class GlpiPluginFormcreatorFormsProfiles(models.Model):
    id = models.IntegerField(primary_key=True)
    plugin_formcreator_forms = models.ForeignKey('GlpiPluginFormcreatorForms', on_delete=models.PROTECT)
    profiles = models.ForeignKey('GlpiProfiles', on_delete=models.PROTECT)
    uuid = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_plugin_formcreator_forms_profiles'
        unique_together = ('plugin_formcreator_forms', 'profiles')


class GlpiPluginFormcreatorFormsValidators(models.Model):
    id = models.IntegerField(primary_key=True)
    plugin_formcreator_forms = models.ForeignKey('GlpiPluginFormcreatorForms', on_delete=models.PROTECT)
    itemtype = models.CharField(max_length=255)
    items_id = models.IntegerField()
    uuid = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_plugin_formcreator_forms_validators'
        unique_together = ('plugin_formcreator_forms', 'itemtype', 'items_id')


class GlpiPluginFormcreatorIssues(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    display_id = models.CharField(max_length=255)
    original_id = models.IntegerField()
    sub_itemtype = models.CharField(max_length=100)
    status = models.CharField(max_length=255)
    date_creation = models.DateTimeField()
    date_mod = models.DateTimeField()
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    requester_id = models.IntegerField()
    users_id_validator = models.IntegerField()
    groups_id_validator = models.IntegerField()
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_plugin_formcreator_issues'


class GlpiPluginFormcreatorItemsTargettickets(models.Model):
    id = models.IntegerField(primary_key=True)
    plugin_formcreator_targettickets = models.ForeignKey('GlpiTickets', on_delete=models.PROTECT)
    link = models.IntegerField()
    itemtype = models.CharField(max_length=255)
    items_id = models.IntegerField()
    uuid = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_plugin_formcreator_items_targettickets'


class GlpiPluginFormcreatorQuestiondependencies(models.Model):
    id = models.IntegerField(primary_key=True)
    plugin_formcreator_questions = models.ForeignKey('GlpiPluginFormcreatorQuestions', on_delete=models.PROTECT)
    plugin_formcreator_questions_id_2 = models.ForeignKey('GlpiPluginFormcreatorQuestions', on_delete=models.PROTECT, related_name='plugin_formcreator_questions_id_2')
    fieldname = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_plugin_formcreator_questiondependencies'


class GlpiPluginFormcreatorQuestionranges(models.Model):
    id = models.IntegerField(primary_key=True)
    plugin_formcreator_questions = models.ForeignKey('GlpiPluginFormcreatorQuestions', on_delete=models.PROTECT)
    range_min = models.CharField(max_length=255, blank=True, null=True)
    range_max = models.CharField(max_length=255, blank=True, null=True)
    fieldname = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_plugin_formcreator_questionranges'


class GlpiPluginFormcreatorQuestionregexes(models.Model):
    id = models.IntegerField(primary_key=True)
    plugin_formcreator_questions = models.ForeignKey('GlpiPluginFormcreatorQuestions', on_delete=models.PROTECT)
    regex = models.TextField(blank=True, null=True)
    fieldname = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_plugin_formcreator_questionregexes'


class GlpiPluginFormcreatorQuestions(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    plugin_formcreator_sections = models.ForeignKey('GlpiPluginFormcreatorSections', on_delete=models.PROTECT)
    fieldtype = models.CharField(max_length=30)
    required = models.IntegerField()
    show_empty = models.IntegerField()
    default_values = models.TextField(blank=True, null=True)
    values = models.TextField(blank=True, null=True)
    description = models.TextField()
    order = models.IntegerField()
    show_rule = models.IntegerField()
    uuid = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_plugin_formcreator_questions'


class GlpiPluginFormcreatorSections(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    plugin_formcreator_forms = models.ForeignKey('GlpiPluginFormcreatorForms', on_delete=models.PROTECT)
    order = models.IntegerField()
    show_rule = models.IntegerField()
    uuid = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_plugin_formcreator_sections'


class GlpiPluginFormcreatorTargetchanges(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    plugin_formcreator_forms = models.ForeignKey('GlpiPluginFormcreatorForms', on_delete=models.PROTECT)
    target_name = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    impactcontent = models.TextField(blank=True, null=True)
    controlistcontent = models.TextField(blank=True, null=True)
    rolloutplancontent = models.TextField(blank=True, null=True)
    backoutplancontent = models.TextField(blank=True, null=True)
    checklistcontent = models.TextField(blank=True, null=True)
    due_date_rule = models.IntegerField()
    due_date_question = models.IntegerField(blank=True, null=True)
    due_date_value = models.IntegerField(blank=True, null=True)
    due_date_period = models.IntegerField()
    urgency_rule = models.IntegerField()
    urgency_question = models.IntegerField()
    validation_followup = models.IntegerField()
    destination_entity = models.IntegerField()
    destination_entity_value = models.IntegerField(blank=True, null=True)
    tag_type = models.IntegerField()
    tag_questions = models.CharField(max_length=255)
    tag_specifics = models.CharField(max_length=255)
    category_rule = models.IntegerField()
    category_question = models.IntegerField()
    show_rule = models.IntegerField()
    uuid = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_plugin_formcreator_targetchanges'


class GlpiPluginFormcreatorTargetchangesActors(models.Model):
    id = models.IntegerField(primary_key=True)
    plugin_formcreator_targetchanges = models.ForeignKey('GlpiChanges', on_delete=models.PROTECT)
    actor_role = models.IntegerField()
    actor_type = models.IntegerField()
    actor_value = models.IntegerField(blank=True, null=True)
    use_notification = models.IntegerField()
    uuid = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_plugin_formcreator_targetchanges_actors'


class GlpiPluginFormcreatorTargettickets(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    plugin_formcreator_forms = models.ForeignKey('GlpiPluginFormcreatorForms', on_delete=models.PROTECT)
    target_name = models.CharField(max_length=255)
    type_rule = models.IntegerField()
    type_question = models.IntegerField()
    tickettemplates = models.ForeignKey('GlpiTicketTemplates', on_delete=models.SET_NULL, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    due_date_rule = models.IntegerField()
    due_date_question = models.IntegerField(blank=True, null=True)
    due_date_value = models.IntegerField(blank=True, null=True)
    due_date_period = models.IntegerField()
    urgency_rule = models.IntegerField()
    urgency_question = models.IntegerField()
    validation_followup = models.IntegerField()
    destination_entity = models.IntegerField()
    destination_entity_value = models.IntegerField(blank=True, null=True)
    tag_type = models.IntegerField()
    tag_questions = models.CharField(max_length=255)
    tag_specifics = models.CharField(max_length=255)
    category_rule = models.IntegerField()
    category_question = models.IntegerField()
    associate_rule = models.IntegerField()
    associate_question = models.IntegerField()
    uuid = models.CharField(max_length=255, blank=True, null=True)
    location_rule = models.IntegerField()
    location_question = models.IntegerField()
    show_rule = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_plugin_formcreator_targettickets'


class GlpiPluginFormcreatorTargetticketsActors(models.Model):
    id = models.IntegerField(primary_key=True)
    plugin_formcreator_targettickets = models.ForeignKey('GlpiTickets', on_delete=models.PROTECT)
    actor_role = models.IntegerField()
    actor_type = models.IntegerField()
    actor_value = models.IntegerField(blank=True, null=True)
    use_notification = models.IntegerField()
    uuid = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_plugin_formcreator_targettickets_actors'


class GlpiPluginGenericobjectTypefamilies(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_plugin_genericobject_typefamilies'


class GlpiPluginGenericobjectTypes(models.Model):
    id = models.IntegerField(primary_key=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    itemtype = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    use_global_search = models.IntegerField()
    use_unicity = models.IntegerField()
    use_history = models.IntegerField()
    use_infocoms = models.IntegerField()
    use_contracts = models.IntegerField()
    use_documents = models.IntegerField()
    use_tickets = models.IntegerField()
    use_links = models.IntegerField()
    use_loans = models.IntegerField()
    use_network_ports = models.IntegerField()
    use_direct_connections = models.IntegerField()
    use_plugin_datainjection = models.IntegerField()
    use_plugin_pdf = models.IntegerField()
    use_plugin_order = models.IntegerField()
    use_plugin_uninstall = models.IntegerField()
    use_plugin_geninventorynumber = models.IntegerField()
    use_menu_entry = models.IntegerField()
    use_projects = models.IntegerField()
    linked_itemtypes = models.TextField(blank=True, null=True)
    plugin_genericobject_typefamilies = models.ForeignKey('GlpiPluginGenericobjectTypefamilies', on_delete=models.PROTECT)
    use_notepad = models.IntegerField()
    use_plugin_simcard = models.IntegerField()
    use_plugin_treeview = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_plugin_genericobject_types'


class GlpiPluginMetabaseProfilerights(models.Model):
    id = models.IntegerField(primary_key=True)
    profiles = models.ForeignKey('GlpiProfiles', on_delete=models.PROTECT)
    dashboard_uuid = models.IntegerField()
    rights = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_plugin_metabase_profilerights'
        unique_together = ('profiles', 'dashboard_uuid')


class GlpiPluginMreportingConfigs(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    classname = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.IntegerField()
    is_notified = models.IntegerField()
    show_graph = models.IntegerField()
    show_area = models.IntegerField()
    spline = models.IntegerField()
    show_label = models.CharField(max_length=10, blank=True, null=True)
    flip_data = models.IntegerField()
    unit = models.CharField(max_length=10, blank=True, null=True)
    default_delay = models.CharField(max_length=10, blank=True, null=True)
    condition = models.CharField(max_length=255, blank=True, null=True)
    graphtype = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_plugin_mreporting_configs'


class GlpiPluginMreportingDashboards(models.Model):
    id = models.IntegerField(primary_key=True)
    users = models.ForeignKey('GlpiUsers', on_delete=models.PROTECT)
    reports_id = models.IntegerField()
    configuration = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_plugin_mreporting_dashboards'


class GlpiPluginMreportingNotifications(models.Model):
    id = models.IntegerField(primary_key=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    notepad = models.TextField(blank=True, null=True)
    date_envoie = models.DateField(blank=True, null=True)
    notice = models.IntegerField()
    alert = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_plugin_mreporting_notifications'


class GlpiPluginMreportingPreferences(models.Model):
    id = models.IntegerField(primary_key=True)
    users = models.ForeignKey('GlpiUsers', on_delete=models.PROTECT)
    template = models.CharField(max_length=255, blank=True, null=True)
    selectors = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_plugin_mreporting_preferences'


class GlpiPluginMreportingProfiles(models.Model):
    id = models.IntegerField(primary_key=True)
    profiles = models.ForeignKey('GlpiProfiles', on_delete=models.PROTECT)
    reports = models.IntegerField()
    right = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_plugin_mreporting_profiles'
        unique_together = ('profiles', 'reports')


class GlpiPluginTreeviewConfigs(models.Model):
    id = models.IntegerField(primary_key=True)
    target = models.CharField(max_length=255)
    folderlinks = models.IntegerField(db_column='folderLinks')  # Field name made lowercase.
    useselection = models.IntegerField(db_column='useSelection')  # Field name made lowercase.
    uselines = models.IntegerField(db_column='useLines')  # Field name made lowercase.
    useicons = models.IntegerField(db_column='useIcons')  # Field name made lowercase.
    closesamelevel = models.IntegerField(db_column='closeSameLevel')  # Field name made lowercase.
    itemname = models.IntegerField(db_column='itemName')  # Field name made lowercase.
    locationname = models.IntegerField(db_column='locationName')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'glpi_plugin_treeview_configs'


class GlpiPluginTreeviewPreferences(models.Model):
    id = models.IntegerField(primary_key=True)
    users = models.ForeignKey('GlpiUsers', on_delete=models.PROTECT)
    show_on_load = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_plugin_treeview_preferences'


class GlpiPluginTreeviewProfiles(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    treeview = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_plugin_treeview_profiles'


class GlpiPluginWebresourcesCategories(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_plugin_webresources_categories'


class GlpiPluginWebresourcesResources(models.Model):
    id = models.IntegerField(primary_key=True)
    users = models.ForeignKey('GlpiUsers', on_delete=models.PROTECT)
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    icon = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField(max_length=16)
    plugin_webresources_categories = models.ForeignKey('GlpiPluginWebresourcesCategories', on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_plugin_webresources_resources'


class GlpiPluginWebresourcesResourcesEntities(models.Model):
    id = models.IntegerField(primary_key=True)
    plugin_webresources_resources = models.ForeignKey('GlpiPluginWebresourcesResources', on_delete=models.PROTECT)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_plugin_webresources_resources_entities'


class GlpiPluginWebresourcesResourcesGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    plugin_webresources_resources = models.ForeignKey('GlpiPluginWebresourcesResources', on_delete=models.PROTECT)
    groups = models.ForeignKey('GlpiGroups', on_delete=models.PROTECT)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_plugin_webresources_resources_groups'


class GlpiPluginWebresourcesResourcesProfiles(models.Model):
    id = models.IntegerField(primary_key=True)
    plugin_webresources_resources = models.ForeignKey('GlpiPluginWebresourcesResources', on_delete=models.PROTECT)
    profiles = models.ForeignKey('GlpiProfiles', on_delete=models.PROTECT)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_plugin_webresources_resources_profiles'


class GlpiPluginWebresourcesResourcesUsers(models.Model):
    id = models.IntegerField(primary_key=True)
    plugin_webresources_resources = models.ForeignKey('GlpiPluginWebresourcesResources', on_delete=models.PROTECT)
    users = models.ForeignKey('GlpiUsers', on_delete=models.PROTECT)

    class Meta:
        managed = False
        db_table = 'glpi_plugin_webresources_resources_users'


class GlpiPlugins(models.Model):
    id = models.IntegerField(primary_key=True)
    directory = models.CharField(unique=True, max_length=255)
    name = models.CharField(max_length=255)
    version = models.CharField(max_length=255)
    state = models.IntegerField()
    author = models.CharField(max_length=255, blank=True, null=True)
    homepage = models.CharField(max_length=255, blank=True, null=True)
    license = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_plugins'


class GlpiPlugs(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_plugs'


class GlpiPrintermodels(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_printermodels'


class GlpiPrinters(models.Model):
    id = models.IntegerField(primary_key=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    contact = models.CharField(max_length=255, blank=True, null=True)
    contact_num = models.CharField(max_length=255, blank=True, null=True)
    users_id_tech = models.IntegerField()
    groups_id_tech = models.IntegerField()
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    have_serial = models.IntegerField()
    have_parallel = models.IntegerField()
    have_usb = models.IntegerField()
    have_wifi = models.IntegerField()
    have_ethernet = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    memory_size = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey('GlpiLocations', on_delete=models.PROTECT)
    networks = models.ForeignKey('GlpiNetworks', on_delete=models.PROTECT)
    printertypes = models.ForeignKey('GlpiPrintertypes', on_delete=models.PROTECT)
    printermodels = models.ForeignKey('GlpiPrintermodels', on_delete=models.PROTECT)
    manufacturers = models.ForeignKey('GlpiManufacturers', on_delete=models.PROTECT)
    is_global = models.IntegerField()
    is_deleted = models.IntegerField()
    is_template = models.IntegerField()
    template_name = models.CharField(max_length=255, blank=True, null=True)
    init_pages_counter = models.IntegerField()
    last_pages_counter = models.IntegerField()
    users = models.ForeignKey('GlpiUsers', on_delete=models.PROTECT)
    groups = models.ForeignKey('GlpiGroups', on_delete=models.PROTECT)
    states = models.ForeignKey('GlpiStates', on_delete=models.PROTECT)
    ticket_tco = models.DecimalField(max_digits=20, decimal_places=4, blank=True, null=True)
    is_dynamic = models.IntegerField()
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_printers'


class GlpiPrintertypes(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_printertypes'


class GlpiProblemcosts(models.Model):
    id = models.IntegerField(primary_key=True)
    problems = models.ForeignKey('GlpiProblems', on_delete=models.PROTECT)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    begin_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    actiontime = models.IntegerField()
    cost_time = models.DecimalField(max_digits=20, decimal_places=4)
    cost_fixed = models.DecimalField(max_digits=20, decimal_places=4)
    cost_material = models.DecimalField(max_digits=20, decimal_places=4)
    budgets = models.ForeignKey('GlpiBudgets', on_delete=models.PROTECT)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)

    class Meta:
        managed = False
        db_table = 'glpi_problemcosts'


class GlpiProblems(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    is_deleted = models.IntegerField()
    status = models.IntegerField()
    content = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    solvedate = models.DateTimeField(blank=True, null=True)
    closedate = models.DateTimeField(blank=True, null=True)
    time_to_resolve = models.DateTimeField(blank=True, null=True)
    users_id_recipient = models.IntegerField()
    users_id_lastupdater = models.IntegerField()
    urgency = models.IntegerField()
    impact = models.IntegerField()
    priority = models.IntegerField()
    itilcategories = models.ForeignKey('GlpiItilcategories', on_delete=models.PROTECT)
    impactcontent = models.TextField(blank=True, null=True)
    causecontent = models.TextField(blank=True, null=True)
    symptomcontent = models.TextField(blank=True, null=True)
    actiontime = models.IntegerField()
    begin_waiting_date = models.DateTimeField(blank=True, null=True)
    waiting_duration = models.IntegerField()
    close_delay_stat = models.IntegerField()
    solve_delay_stat = models.IntegerField()
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_problems'


class GlpiProblemsSuppliers(models.Model):
    id = models.IntegerField(primary_key=True)
    problems = models.ForeignKey('GlpiProblems', on_delete=models.PROTECT)
    suppliers = models.ForeignKey('GlpiSuppliers', on_delete=models.PROTECT)
    type = models.IntegerField()
    use_notification = models.IntegerField()
    alternative_email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_problems_suppliers'
        unique_together = ('problems', 'type', 'suppliers')


class GlpiProblemsTickets(models.Model):
    id = models.IntegerField(primary_key=True)
    problems = models.ForeignKey('GlpiProblems', on_delete=models.PROTECT)
    tickets = models.ForeignKey('GlpiTickets', on_delete=models.PROTECT)

    class Meta:
        managed = False
        db_table = 'glpi_problems_tickets'
        unique_together = ('problems', 'tickets')


class GlpiProblemsUsers(models.Model):
    id = models.IntegerField(primary_key=True)
    problems = models.ForeignKey('GlpiProblems', on_delete=models.PROTECT)
    users = models.ForeignKey('GlpiUsers', on_delete=models.PROTECT)
    type = models.IntegerField()
    use_notification = models.IntegerField()
    alternative_email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_problems_users'
        unique_together = ('problems', 'type', 'users', 'alternative_email')


class GlpiProblemtasks(models.Model):
    id = models.IntegerField(primary_key=True)
    uuid = models.CharField(unique=True, max_length=255, blank=True, null=True)
    problems = models.ForeignKey('GlpiProblems', on_delete=models.PROTECT)
    taskcategories = models.ForeignKey('GlpiTaskcategories', on_delete=models.PROTECT)
    date = models.DateTimeField(blank=True, null=True)
    begin = models.DateTimeField(blank=True, null=True)
    end = models.DateTimeField(blank=True, null=True)
    users = models.ForeignKey('GlpiUsers', on_delete=models.PROTECT)
    users_id_editor = models.IntegerField()
    users_id_tech = models.IntegerField()
    groups_id_tech = models.IntegerField()
    content = models.TextField(blank=True, null=True)
    actiontime = models.IntegerField()
    state = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    tasktemplates = models.ForeignKey('GlpiTasktemplates', on_delete=models.PROTECT)
    timeline_position = models.IntegerField()
    is_private = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_problemtasks'


class GlpiProblemtemplatehiddenfields(models.Model):
    id = models.IntegerField(primary_key=True)
    problemtemplates = models.ForeignKey('GlpiProblemtemplates', on_delete=models.PROTECT)
    num = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_problemtemplatehiddenfields'
        unique_together = ('problemtemplates', 'num')


class GlpiProblemtemplatemandatoryfields(models.Model):
    id = models.IntegerField(primary_key=True)
    problemtemplates = models.ForeignKey('GlpiProblemtemplates', on_delete=models.PROTECT)
    num = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_problemtemplatemandatoryfields'
        unique_together = ('problemtemplates', 'num')


class GlpiProblemtemplatepredefinedfields(models.Model):
    id = models.IntegerField(primary_key=True)
    problemtemplates = models.ForeignKey('GlpiProblemtemplates', on_delete=models.PROTECT)
    num = models.IntegerField()
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_problemtemplatepredefinedfields'


class GlpiProblemtemplates(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_problemtemplates'


class GlpiProfilerights(models.Model):
    id = models.IntegerField(primary_key=True)
    profiles = models.ForeignKey('GlpiProfiles', on_delete=models.PROTECT)
    name = models.CharField(max_length=255, blank=True, null=True)
    rights = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_profilerights'
        unique_together = ('profiles', 'name')


class GlpiProfiles(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    interface = models.CharField(max_length=255, blank=True, null=True)
    is_default = models.IntegerField()
    helpdesk_hardware = models.IntegerField()
    helpdesk_item_type = models.TextField(blank=True, null=True)
    ticket_status = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    problem_status = models.TextField(blank=True, null=True)
    create_ticket_on_login = models.IntegerField()
    tickettemplates = models.ForeignKey('GlpiTickettemplates', on_delete=models.PROTECT)
    changetemplates = models.ForeignKey('GlpiChangetemplates', on_delete=models.PROTECT)
    problemtemplates = models.ForeignKey('GlpiProblemtemplates', on_delete=models.PROTECT)
    change_status = models.TextField(blank=True, null=True)
    managed_domainrecordtypes = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_profiles'


class GlpiProfilesReminders(models.Model):
    id = models.IntegerField(primary_key=True)
    reminders = models.ForeignKey('GlpiReminders', on_delete=models.PROTECT)
    profiles = models.ForeignKey('GlpiProfiles', on_delete=models.PROTECT)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_profiles_reminders'


class GlpiProfilesRssfeeds(models.Model):
    id = models.IntegerField(primary_key=True)
    rssfeeds = models.ForeignKey('GlpiRssfeeds', on_delete=models.PROTECT)
    profiles = models.ForeignKey('GlpiProfiles', on_delete=models.PROTECT)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_profiles_rssfeeds'


class GlpiProfilesUsers(models.Model):
    id = models.IntegerField(primary_key=True)
    users = models.ForeignKey('GlpiUsers', on_delete=models.PROTECT)
    profiles = models.ForeignKey('GlpiProfiles', on_delete=models.PROTECT)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    is_dynamic = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_profiles_users'


class GlpiProjectcosts(models.Model):
    id = models.IntegerField(primary_key=True)
    projects = models.ForeignKey('GlpiProjects', on_delete=models.PROTECT)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    begin_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    cost = models.DecimalField(max_digits=20, decimal_places=4)
    budgets = models.ForeignKey('GlpiBudgets', on_delete=models.PROTECT)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_projectcosts'


class GlpiProjects(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    priority = models.IntegerField()
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    projects = models.ForeignKey('GlpiProjects', on_delete=models.PROTECT)
    projectstates = models.ForeignKey('GlpiStates', on_delete=models.PROTECT)
    projecttypes = models.ForeignKey('GlpiProjecttypes', on_delete=models.PROTECT)
    date = models.DateTimeField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    users = models.ForeignKey('GlpiUsers', on_delete=models.PROTECT)
    groups = models.ForeignKey('GlpiGroups', on_delete=models.PROTECT)
    plan_start_date = models.DateTimeField(blank=True, null=True)
    plan_end_date = models.DateTimeField(blank=True, null=True)
    real_start_date = models.DateTimeField(blank=True, null=True)
    real_end_date = models.DateTimeField(blank=True, null=True)
    percent_done = models.IntegerField()
    auto_percent_done = models.IntegerField()
    show_on_global_gantt = models.IntegerField()
    content = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    is_deleted = models.IntegerField()
    date_creation = models.DateTimeField(blank=True, null=True)
    projecttemplates_id = models.IntegerField()
    is_template = models.IntegerField()
    template_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_projects'


class GlpiProjectstates(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)
    is_finished = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_projectstates'


class GlpiProjecttasks(models.Model):
    id = models.IntegerField(primary_key=True)
    uuid = models.CharField(unique=True, max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    projects = models.ForeignKey('GlpiProjects', on_delete=models.PROTECT)
    projecttasks = models.ForeignKey('GlpiProjecttasks', on_delete=models.PROTECT)
    date = models.DateTimeField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    plan_start_date = models.DateTimeField(blank=True, null=True)
    plan_end_date = models.DateTimeField(blank=True, null=True)
    real_start_date = models.DateTimeField(blank=True, null=True)
    real_end_date = models.DateTimeField(blank=True, null=True)
    planned_duration = models.IntegerField()
    effective_duration = models.IntegerField()
    projectstates = models.ForeignKey('GlpiStates', on_delete=models.PROTECT)
    projecttasktypes = models.ForeignKey('GlpiProjecttasktypes', on_delete=models.PROTECT)
    users = models.ForeignKey('GlpiUsers', on_delete=models.PROTECT)
    percent_done = models.IntegerField()
    auto_percent_done = models.IntegerField()
    is_milestone = models.IntegerField()
    projecttasktemplates = models.ForeignKey('GlpiTasktemplates', on_delete=models.PROTECT)
    is_template = models.IntegerField()
    template_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_projecttasks'


class GlpiProjecttasksTickets(models.Model):
    id = models.IntegerField(primary_key=True)
    tickets = models.ForeignKey('GlpiTickets', on_delete=models.PROTECT)
    projecttasks = models.ForeignKey('GlpiProjecttasks', on_delete=models.PROTECT)

    class Meta:
        managed = False
        db_table = 'glpi_projecttasks_tickets'
        unique_together = ('tickets', 'projecttasks')


class GlpiProjecttaskteams(models.Model):
    id = models.IntegerField(primary_key=True)
    projecttasks = models.ForeignKey('GlpiProjecttasks', on_delete=models.PROTECT)
    itemtype = models.CharField(max_length=100, blank=True, null=True)
    items_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_projecttaskteams'
        unique_together = ('projecttasks', 'itemtype', 'items_id')


class GlpiProjecttasktemplates(models.Model):
    id = models.IntegerField(primary_key=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    projects = models.ForeignKey('GlpiProjects', on_delete=models.PROTECT)
    projecttasks = models.ForeignKey('GlpiProjecttasks', on_delete=models.PROTECT)
    plan_start_date = models.DateTimeField(blank=True, null=True)
    plan_end_date = models.DateTimeField(blank=True, null=True)
    real_start_date = models.DateTimeField(blank=True, null=True)
    real_end_date = models.DateTimeField(blank=True, null=True)
    planned_duration = models.IntegerField()
    effective_duration = models.IntegerField()
    projectstates = models.ForeignKey('GlpiStates', on_delete=models.PROTECT)
    projecttasktypes = models.ForeignKey('GlpiProjecttasktypes', on_delete=models.PROTECT)
    users = models.ForeignKey('GlpiUsers', on_delete=models.PROTECT)
    percent_done = models.IntegerField()
    is_milestone = models.IntegerField()
    comments = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_projecttasktemplates'


class GlpiProjecttasktypes(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_projecttasktypes'


class GlpiProjectteams(models.Model):
    id = models.IntegerField(primary_key=True)
    projects = models.ForeignKey('GlpiProjects', on_delete=models.PROTECT)
    itemtype = models.CharField(max_length=100, blank=True, null=True)
    items_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_projectteams'
        unique_together = ('projects', 'itemtype', 'items_id')


class GlpiProjecttypes(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_projecttypes'


class GlpiQueuednotifications(models.Model):
    id = models.IntegerField(primary_key=True)
    itemtype = models.CharField(max_length=100, blank=True, null=True)
    items_id = models.IntegerField()
    notificationtemplates = models.ForeignKey('GlpiNotificationtemplates', on_delete=models.PROTECT)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_deleted = models.IntegerField()
    sent_try = models.IntegerField()
    create_time = models.DateTimeField(blank=True, null=True)
    send_time = models.DateTimeField(blank=True, null=True)
    sent_time = models.DateTimeField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    sender = models.TextField(blank=True, null=True)
    sendername = models.TextField(blank=True, null=True)
    recipient = models.TextField(blank=True, null=True)
    recipientname = models.TextField(blank=True, null=True)
    replyto = models.TextField(blank=True, null=True)
    replytoname = models.TextField(blank=True, null=True)
    headers = models.TextField(blank=True, null=True)
    body_html = models.TextField(blank=True, null=True)
    body_text = models.TextField(blank=True, null=True)
    messageid = models.TextField(blank=True, null=True)
    documents = models.TextField(blank=True, null=True)
    mode = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'glpi_queuednotifications'


class GlpiRackmodels(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_number = models.CharField(max_length=255, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_rackmodels'


class GlpiRacks(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    locations = models.ForeignKey('GlpiLocations', on_delete=models.PROTECT)
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    rackmodels = models.ForeignKey('GlpiRackmodels', on_delete=models.SET_NULL, blank=True, null=True)
    manufacturers = models.ForeignKey('GlpiManufacturers', on_delete=models.PROTECT)
    racktypes = models.ForeignKey('GlpiRacktypes', on_delete=models.PROTECT)
    states = models.ForeignKey('GlpiStates', on_delete=models.PROTECT)
    users_id_tech = models.IntegerField()
    groups_id_tech = models.IntegerField()
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    depth = models.IntegerField(blank=True, null=True)
    number_units = models.IntegerField(blank=True, null=True)
    is_template = models.IntegerField()
    template_name = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.IntegerField()
    dcrooms = models.ForeignKey('GlpiDcrooms', on_delete=models.PROTECT)
    room_orientation = models.IntegerField()
    position = models.CharField(max_length=50, blank=True, null=True)
    bgcolor = models.CharField(max_length=7, blank=True, null=True)
    max_power = models.IntegerField()
    mesured_power = models.IntegerField()
    max_weight = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_racks'


class GlpiRacktypes(models.Model):
    id = models.IntegerField(primary_key=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_racktypes'


class GlpiRegisteredids(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    items_id = models.IntegerField()
    itemtype = models.CharField(max_length=100)
    device_type = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'glpi_registeredids'


class GlpiReminders(models.Model):
    id = models.IntegerField(primary_key=True)
    uuid = models.CharField(unique=True, max_length=255, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    users = models.ForeignKey('GlpiUsers', on_delete=models.PROTECT)
    name = models.CharField(max_length=255, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    begin = models.DateTimeField(blank=True, null=True)
    end = models.DateTimeField(blank=True, null=True)
    is_planned = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    state = models.IntegerField()
    begin_view_date = models.DateTimeField(blank=True, null=True)
    end_view_date = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_reminders'


class GlpiRemindersUsers(models.Model):
    id = models.IntegerField(primary_key=True)
    reminders = models.ForeignKey('GlpiReminders', on_delete=models.PROTECT)
    users = models.ForeignKey('GlpiUsers', on_delete=models.PROTECT)

    class Meta:
        managed = False
        db_table = 'glpi_reminders_users'


class GlpiRemindertranslations(models.Model):
    id = models.IntegerField(primary_key=True)
    reminders = models.ForeignKey('GlpiReminders', on_delete=models.PROTECT)
    language = models.CharField(max_length=5, blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    users = models.ForeignKey('GlpiUsers', on_delete=models.PROTECT)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_remindertranslations'


class GlpiRequesttypes(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    is_helpdesk_default = models.IntegerField()
    is_followup_default = models.IntegerField()
    is_mail_default = models.IntegerField()
    is_mailfollowup_default = models.IntegerField()
    is_active = models.IntegerField()
    is_ticketheader = models.IntegerField()
    is_itilfollowup = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_requesttypes'


class GlpiReservationitems(models.Model):
    id = models.IntegerField(primary_key=True)
    itemtype = models.CharField(max_length=100)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    items_id = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    is_active = models.IntegerField()
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_reservationitems'


class GlpiReservations(models.Model):
    id = models.IntegerField(primary_key=True)
    reservationitems = models.ForeignKey('GlpiReservationitems', on_delete=models.PROTECT)
    begin = models.DateTimeField(blank=True, null=True)
    end = models.DateTimeField(blank=True, null=True)
    users = models.ForeignKey('GlpiUsers', on_delete=models.PROTECT)
    comment = models.TextField(blank=True, null=True)
    group = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_reservations'


class GlpiRssfeeds(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    users = models.ForeignKey('GlpiUsers', on_delete=models.PROTECT)
    comment = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    refresh_rate = models.IntegerField()
    max_items = models.IntegerField()
    have_error = models.IntegerField()
    is_active = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_rssfeeds'


class GlpiRssfeedsUsers(models.Model):
    id = models.IntegerField(primary_key=True)
    rssfeeds = models.ForeignKey('GlpiRssfeeds', on_delete=models.PROTECT)
    users = models.ForeignKey('GlpiUsers', on_delete=models.PROTECT)

    class Meta:
        managed = False
        db_table = 'glpi_rssfeeds_users'


class GlpiRuleactions(models.Model):
    id = models.IntegerField(primary_key=True)
    rules = models.ForeignKey('GlpiRules', on_delete=models.PROTECT)
    action_type = models.CharField(max_length=255, blank=True, null=True)
    field = models.CharField(max_length=255, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_ruleactions'


class GlpiRulecriterias(models.Model):
    id = models.IntegerField(primary_key=True)
    rules = models.ForeignKey('GlpiRules', on_delete=models.PROTECT)
    criteria = models.CharField(max_length=255, blank=True, null=True)
    condition = models.IntegerField()
    pattern = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_rulecriterias'


class GlpiRulerightparameters(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_rulerightparameters'


class GlpiRules(models.Model):
    id = models.IntegerField(primary_key=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    sub_type = models.CharField(max_length=255)
    ranking = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    match = models.CharField(max_length=10, blank=True, null=True)
    is_active = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    is_recursive = models.IntegerField()
    uuid = models.CharField(max_length=255, blank=True, null=True)
    condition = models.IntegerField()
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_rules'


class GlpiSavedsearches(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    type = models.IntegerField()
    itemtype = models.CharField(max_length=100)
    users = models.ForeignKey('GlpiUsers', on_delete=models.PROTECT)
    is_private = models.IntegerField()
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    path = models.CharField(max_length=255, blank=True, null=True)
    query = models.TextField(blank=True, null=True)
    last_execution_time = models.IntegerField(blank=True, null=True)
    do_count = models.IntegerField()
    last_execution_date = models.DateTimeField(blank=True, null=True)
    counter = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_savedsearches'


class GlpiSavedsearchesAlerts(models.Model):
    id = models.IntegerField(primary_key=True)
    savedsearches = models.ForeignKey('GlpiSavedsearches', on_delete=models.PROTECT)
    name = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.IntegerField()
    operator = models.IntegerField()
    value = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_savedsearches_alerts'
        unique_together = ('savedsearches', 'operator', 'value')


class GlpiSavedsearchesUsers(models.Model):
    id = models.IntegerField(primary_key=True)
    users = models.ForeignKey('GlpiUsers', on_delete=models.PROTECT)
    itemtype = models.CharField(max_length=100)
    savedsearches = models.ForeignKey('GlpiSavedsearches', on_delete=models.PROTECT)

    class Meta:
        managed = False
        db_table = 'glpi_savedsearches_users'
        unique_together = ('users', 'itemtype')


class GlpiSlalevelactions(models.Model):
    id = models.IntegerField(primary_key=True)
    slalevels = models.ForeignKey('GlpiSlalevels', on_delete=models.PROTECT)
    action_type = models.CharField(max_length=255, blank=True, null=True)
    field = models.CharField(max_length=255, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_slalevelactions'


class GlpiSlalevelcriterias(models.Model):
    id = models.IntegerField(primary_key=True)
    slalevels = models.ForeignKey('GlpiSlalevels', on_delete=models.PROTECT)
    criteria = models.CharField(max_length=255, blank=True, null=True)
    condition = models.IntegerField()
    pattern = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_slalevelcriterias'


class GlpiSlalevels(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    slas = models.ForeignKey('GlpiSlas', on_delete=models.PROTECT)
    execution_time = models.IntegerField()
    is_active = models.IntegerField()
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    match = models.CharField(max_length=10, blank=True, null=True)
    uuid = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_slalevels'


class GlpiSlalevelsTickets(models.Model):
    id = models.IntegerField(primary_key=True)
    tickets = models.ForeignKey('GlpiTickets', on_delete=models.PROTECT)
    slalevels = models.ForeignKey('GlpiSlalevels', on_delete=models.PROTECT)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_slalevels_tickets'
        unique_together = ('tickets', 'slalevels')


class GlpiSlas(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    type = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    number_time = models.IntegerField()
    calendars = models.ForeignKey('GlpiCalendars', on_delete=models.PROTECT)
    date_mod = models.DateTimeField(blank=True, null=True)
    definition_time = models.CharField(max_length=255, blank=True, null=True)
    end_of_working_day = models.IntegerField()
    date_creation = models.DateTimeField(blank=True, null=True)
    slms = models.ForeignKey('GlpiSlms', on_delete=models.PROTECT)

    class Meta:
        managed = False
        db_table = 'glpi_slas'


class GlpiSlms(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    calendars = models.ForeignKey('GlpiCalendars', on_delete=models.PROTECT)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_slms'


class GlpiSoftwarecategories(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    softwarecategories = models.ForeignKey('self', on_delete=models.PROTECT)
    completename = models.TextField(blank=True, null=True)
    level = models.IntegerField()
    ancestors_cache = models.TextField(blank=True, null=True)
    sons_cache = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_softwarecategories'


class GlpiSoftwarelicenses(models.Model):
    id = models.IntegerField(primary_key=True)
    softwares = models.ForeignKey('GlpiSoftwares', on_delete=models.PROTECT)
    softwarelicenses = models.ForeignKey('self', on_delete=models.PROTECT)
    completename = models.TextField(blank=True, null=True)
    level = models.IntegerField()
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    number = models.IntegerField()
    softwarelicensetypes = models.ForeignKey('GlpiSoftwarelicensetypes', on_delete=models.PROTECT)
    name = models.CharField(max_length=255, blank=True, null=True)
    serial = models.CharField(max_length=255, blank=True, null=True)
    otherserial = models.CharField(max_length=255, blank=True, null=True)
    softwareversions_id_buy = models.IntegerField()
    softwareversions_id_use = models.IntegerField()
    expire = models.DateField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    is_valid = models.IntegerField()
    date_creation = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    locations = models.ForeignKey('GlpiLocations', on_delete=models.PROTECT)
    users_id_tech = models.IntegerField()
    users = models.ForeignKey('GlpiUsers', on_delete=models.PROTECT)
    groups_id_tech = models.IntegerField()
    groups = models.ForeignKey('GlpiGroups', on_delete=models.PROTECT)
    is_helpdesk_visible = models.IntegerField()
    is_template = models.IntegerField()
    template_name = models.CharField(max_length=255, blank=True, null=True)
    states = models.ForeignKey('GlpiStates', on_delete=models.PROTECT)
    manufacturers = models.ForeignKey('GlpiManufacturers', on_delete=models.PROTECT)
    contact = models.CharField(max_length=255, blank=True, null=True)
    contact_num = models.CharField(max_length=255, blank=True, null=True)
    allow_overquota = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_softwarelicenses'


class GlpiSoftwarelicensetypes(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    softwarelicensetypes = models.ForeignKey('self', on_delete=models.PROTECT)
    level = models.IntegerField()
    ancestors_cache = models.TextField(blank=True, null=True)
    sons_cache = models.TextField(blank=True, null=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    completename = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_softwarelicensetypes'


class GlpiSoftwares(models.Model):
    id = models.IntegerField(primary_key=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    locations = models.ForeignKey('GlpiLocations', on_delete=models.PROTECT)
    users_id_tech = models.IntegerField()
    groups_id_tech = models.IntegerField()
    is_update = models.IntegerField()
    softwares = models.ForeignKey('GlpiSoftwares', on_delete=models.PROTECT)
    manufacturers = models.ForeignKey('GlpiManufacturers', on_delete=models.PROTECT)
    is_deleted = models.IntegerField()
    is_template = models.IntegerField()
    template_name = models.CharField(max_length=255, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    users = models.ForeignKey('GlpiUsers', on_delete=models.PROTECT)
    groups = models.ForeignKey('GlpiGroups', on_delete=models.PROTECT)
    ticket_tco = models.DecimalField(max_digits=20, decimal_places=4, blank=True, null=True)
    is_helpdesk_visible = models.IntegerField()
    softwarecategories = models.ForeignKey('GlpiSoftwarecategories', on_delete=models.PROTECT)
    is_valid = models.IntegerField()
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_softwares'


class GlpiSoftwareversions(models.Model):
    id = models.IntegerField(primary_key=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    softwares = models.ForeignKey('GlpiSoftwares', on_delete=models.PROTECT)
    states = models.ForeignKey('GlpiStates', on_delete=models.PROTECT)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    operatingsystems = models.ForeignKey('GlpiOperatingsystems', on_delete=models.PROTECT)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_softwareversions'


class GlpiSolutiontemplates(models.Model):
    id = models.IntegerField(primary_key=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    solutiontypes = models.ForeignKey('GlpiSolutiontypes', on_delete=models.PROTECT)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_solutiontemplates'


class GlpiSolutiontypes(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_solutiontypes'


class GlpiSsovariables(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_ssovariables'


class GlpiStates(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    states = models.ForeignKey('GlpiStates', on_delete=models.PROTECT)
    completename = models.TextField(blank=True, null=True)
    level = models.IntegerField()
    ancestors_cache = models.TextField(blank=True, null=True)
    sons_cache = models.TextField(blank=True, null=True)
    is_visible_computer = models.IntegerField()
    is_visible_monitor = models.IntegerField()
    is_visible_networkequipment = models.IntegerField()
    is_visible_peripheral = models.IntegerField()
    is_visible_phone = models.IntegerField()
    is_visible_printer = models.IntegerField()
    is_visible_softwareversion = models.IntegerField()
    is_visible_softwarelicense = models.IntegerField()
    is_visible_line = models.IntegerField()
    is_visible_certificate = models.IntegerField()
    is_visible_rack = models.IntegerField()
    is_visible_passivedcequipment = models.IntegerField()
    is_visible_enclosure = models.IntegerField()
    is_visible_pdu = models.IntegerField()
    is_visible_cluster = models.IntegerField()
    is_visible_contract = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_states'
        unique_together = ('states', 'name')


class GlpiSuppliers(models.Model):
    id = models.IntegerField(primary_key=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    suppliertypes = models.ForeignKey('GlpiSuppliertypes', on_delete=models.PROTECT)
    address = models.TextField(blank=True, null=True)
    postcode = models.CharField(max_length=255, blank=True, null=True)
    town = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    phonenumber = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    is_deleted = models.IntegerField()
    fax = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    is_active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_suppliers'


class GlpiSuppliersTickets(models.Model):
    id = models.IntegerField(primary_key=True)
    tickets = models.ForeignKey('GlpiTickets', on_delete=models.PROTECT)
    suppliers = models.ForeignKey('GlpiSuppliers', on_delete=models.PROTECT)
    type = models.IntegerField()
    use_notification = models.IntegerField()
    alternative_email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_suppliers_tickets'
        unique_together = ('tickets', 'type', 'suppliers')


class GlpiSuppliertypes(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_suppliertypes'


class GlpiTaskcategories(models.Model):
    id = models.IntegerField(primary_key=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    taskcategories = models.ForeignKey('GlpiTaskcategories', on_delete=models.PROTECT)
    name = models.CharField(max_length=255, blank=True, null=True)
    completename = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    level = models.IntegerField()
    ancestors_cache = models.TextField(blank=True, null=True)
    sons_cache = models.TextField(blank=True, null=True)
    is_active = models.IntegerField()
    is_helpdeskvisible = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    knowbaseitemcategories = models.ForeignKey('GlpiKnowbaseitemcategories', on_delete=models.PROTECT)

    class Meta:
        managed = False
        db_table = 'glpi_taskcategories'


class GlpiTasktemplates(models.Model):
    id = models.IntegerField(primary_key=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    taskcategories = models.ForeignKey('GlpiTaskcategories', on_delete=models.PROTECT)
    actiontime = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    state = models.IntegerField()
    is_private = models.IntegerField()
    users_id_tech = models.IntegerField()
    groups_id_tech = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_tasktemplates'


class GlpiTicketcosts(models.Model):
    id = models.IntegerField(primary_key=True)
    tickets = models.ForeignKey('GlpiTickets', on_delete=models.PROTECT)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    begin_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    actiontime = models.IntegerField()
    cost_time = models.DecimalField(max_digits=20, decimal_places=4)
    cost_fixed = models.DecimalField(max_digits=20, decimal_places=4)
    cost_material = models.DecimalField(max_digits=20, decimal_places=4)
    budgets = models.ForeignKey('GlpiBudgets', on_delete=models.PROTECT)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)

    class Meta:
        managed = False
        db_table = 'glpi_ticketcosts'


class GlpiTicketrecurrents(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    is_active = models.IntegerField()
    tickettemplates = models.ForeignKey('GlpiTickettemplates', on_delete=models.PROTECT)
    begin_date = models.DateTimeField(blank=True, null=True)
    periodicity = models.CharField(max_length=255, blank=True, null=True)
    create_before = models.IntegerField()
    next_creation_date = models.DateTimeField(blank=True, null=True)
    calendars = models.ForeignKey('GlpiCalendars', on_delete=models.PROTECT)
    end_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_ticketrecurrents'


class GlpiTickets(models.Model):
    id = models.IntegerField(primary_key=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    name = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    closedate = models.DateTimeField(blank=True, null=True)
    solvedate = models.DateTimeField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    users_id_lastupdater = models.IntegerField()
    status = models.IntegerField()
    users_id_recipient = models.IntegerField()
    requesttypes = models.ForeignKey('GlpiRequesttypes', on_delete=models.PROTECT)
    content = models.TextField(blank=True, null=True)
    urgency = models.IntegerField()
    impact = models.IntegerField()
    priority = models.IntegerField()
    itilcategories = models.ForeignKey('GlpiItilcategories', on_delete=models.PROTECT)
    type = models.IntegerField()
    global_validation = models.IntegerField()
    slas_id_ttr = models.IntegerField()
    slas_id_tto = models.IntegerField()
    slalevels_id_ttr = models.IntegerField()
    time_to_resolve = models.DateTimeField(blank=True, null=True)
    time_to_own = models.DateTimeField(blank=True, null=True)
    begin_waiting_date = models.DateTimeField(blank=True, null=True)
    sla_waiting_duration = models.IntegerField()
    ola_waiting_duration = models.IntegerField()
    olas_id_tto = models.IntegerField()
    olas_id_ttr = models.IntegerField()
    olalevels_id_ttr = models.IntegerField()
    ola_ttr_begin_date = models.DateTimeField(blank=True, null=True)
    internal_time_to_resolve = models.DateTimeField(blank=True, null=True)
    internal_time_to_own = models.DateTimeField(blank=True, null=True)
    waiting_duration = models.IntegerField()
    close_delay_stat = models.IntegerField()
    solve_delay_stat = models.IntegerField()
    takeintoaccount_delay_stat = models.IntegerField()
    actiontime = models.IntegerField()
    is_deleted = models.IntegerField()
    locations = models.ForeignKey('GlpiLocations', on_delete=models.PROTECT)
    validation_percent = models.IntegerField()
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_tickets'


class GlpiTicketsTickets(models.Model):
    id = models.IntegerField(primary_key=True)
    tickets_id_1 = models.IntegerField()
    tickets_id_2 = models.IntegerField()
    link = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_tickets_tickets'
        unique_together = (('tickets_id_1', 'tickets_id_2'),)


class GlpiTicketsUsers(models.Model):
    id = models.IntegerField(primary_key=True)
    tickets = models.ForeignKey('GlpiTickets', on_delete=models.PROTECT)
    users = models.ForeignKey('GlpiUsers', on_delete=models.PROTECT)
    type = models.IntegerField()
    use_notification = models.IntegerField()
    alternative_email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_tickets_users'
        unique_together = ('tickets', 'type', 'users', 'alternative_email')


class GlpiTicketsatisfactions(models.Model):
    id = models.IntegerField(primary_key=True)
    tickets = models.OneToOneField('GlpiTickets', on_delete=models.PROTECT)
    type = models.IntegerField()
    date_begin = models.DateTimeField(blank=True, null=True)
    date_answered = models.DateTimeField(blank=True, null=True)
    satisfaction = models.IntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_ticketsatisfactions'


class GlpiTickettasks(models.Model):
    id = models.IntegerField(primary_key=True)
    uuid = models.CharField(unique=True, max_length=255, blank=True, null=True)
    tickets = models.ForeignKey('GlpiTickets', on_delete=models.PROTECT)
    taskcategories = models.ForeignKey('GlpiTaskcategories', on_delete=models.PROTECT)
    date = models.DateTimeField(blank=True, null=True)
    users = models.ForeignKey('GlpiUsers', on_delete=models.PROTECT)
    users_id_editor = models.IntegerField()
    content = models.TextField(blank=True, null=True)
    is_private = models.IntegerField()
    actiontime = models.IntegerField()
    begin = models.DateTimeField(blank=True, null=True)
    end = models.DateTimeField(blank=True, null=True)
    state = models.IntegerField()
    users_id_tech = models.IntegerField()
    groups_id_tech = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    tasktemplates = models.ForeignKey('GlpiTasktemplates', on_delete=models.PROTECT)
    timeline_position = models.IntegerField()
    sourceitems_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_tickettasks'


class GlpiTickettemplatehiddenfields(models.Model):
    id = models.IntegerField(primary_key=True)
    tickettemplates = models.ForeignKey('GlpiTickettemplates', on_delete=models.PROTECT)
    num = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_tickettemplatehiddenfields'
        unique_together = ('tickettemplates', 'num')


class GlpiTickettemplatemandatoryfields(models.Model):
    id = models.IntegerField(primary_key=True)
    tickettemplates = models.ForeignKey('GlpiTickettemplates', on_delete=models.PROTECT)
    num = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_tickettemplatemandatoryfields'
        unique_together = ('tickettemplates', 'num')


class GlpiTickettemplatepredefinedfields(models.Model):
    id = models.IntegerField(primary_key=True)
    tickettemplates = models.ForeignKey('GlpiTickettemplates', on_delete=models.PROTECT)
    num = models.IntegerField()
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_tickettemplatepredefinedfields'


class GlpiTickettemplates(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_tickettemplates'


class GlpiTicketvalidations(models.Model):
    id = models.IntegerField(primary_key=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    users = models.ForeignKey('GlpiUsers', on_delete=models.PROTECT)
    tickets = models.ForeignKey('GlpiTickets', on_delete=models.PROTECT)
    users_id_validate = models.IntegerField()
    comment_submission = models.TextField(blank=True, null=True)
    comment_validation = models.TextField(blank=True, null=True)
    status = models.IntegerField()
    submission_date = models.DateTimeField(blank=True, null=True)
    validation_date = models.DateTimeField(blank=True, null=True)
    timeline_position = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_ticketvalidations'


class GlpiTransfers(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    keep_ticket = models.IntegerField()
    keep_networklink = models.IntegerField()
    keep_reservation = models.IntegerField()
    keep_history = models.IntegerField()
    keep_device = models.IntegerField()
    keep_infocom = models.IntegerField()
    keep_dc_monitor = models.IntegerField()
    clean_dc_monitor = models.IntegerField()
    keep_dc_phone = models.IntegerField()
    clean_dc_phone = models.IntegerField()
    keep_dc_peripheral = models.IntegerField()
    clean_dc_peripheral = models.IntegerField()
    keep_dc_printer = models.IntegerField()
    clean_dc_printer = models.IntegerField()
    keep_supplier = models.IntegerField()
    clean_supplier = models.IntegerField()
    keep_contact = models.IntegerField()
    clean_contact = models.IntegerField()
    keep_contract = models.IntegerField()
    clean_contract = models.IntegerField()
    keep_software = models.IntegerField()
    clean_software = models.IntegerField()
    keep_document = models.IntegerField()
    clean_document = models.IntegerField()
    keep_cartridgeitem = models.IntegerField()
    clean_cartridgeitem = models.IntegerField()
    keep_cartridge = models.IntegerField()
    keep_consumable = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    keep_disk = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'glpi_transfers'


class GlpiUsercategories(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_usercategories'


class GlpiUseremails(models.Model):
    id = models.IntegerField(primary_key=True)
    users = models.ForeignKey('GlpiUsers', on_delete=models.PROTECT)
    is_default = models.IntegerField()
    is_dynamic = models.IntegerField()
    email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_useremails'
        unique_together = ('users', 'email')


class GlpiUsers(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    password_last_update = models.DateTimeField(blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    phone2 = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=255, blank=True, null=True)
    realname = models.CharField(max_length=255, blank=True, null=True)
    firstname = models.CharField(max_length=255, blank=True, null=True)
    locations = models.ForeignKey('GlpiLocations', on_delete=models.PROTECT)
    language = models.CharField(max_length=10, blank=True, null=True)
    use_mode = models.IntegerField()
    list_limit = models.IntegerField(blank=True, null=True)
    is_active = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    auths_id = models.IntegerField()
    authtype = models.IntegerField()
    last_login = models.DateTimeField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_sync = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    profiles = models.ForeignKey('GlpiProfiles', on_delete=models.PROTECT)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    usertitles = models.ForeignKey('GlpiUsertitles', on_delete=models.PROTECT)
    usercategories = models.ForeignKey('GlpiUsercategories', on_delete=models.PROTECT)
    date_format = models.IntegerField(blank=True, null=True)
    number_format = models.IntegerField(blank=True, null=True)
    names_format = models.IntegerField(blank=True, null=True)
    csv_delimiter = models.CharField(max_length=1, blank=True, null=True)
    is_ids_visible = models.IntegerField(blank=True, null=True)
    use_flat_dropdowntree = models.IntegerField(blank=True, null=True)
    show_jobs_at_login = models.IntegerField(blank=True, null=True)
    priority_1 = models.CharField(max_length=20, blank=True, null=True)
    priority_2 = models.CharField(max_length=20, blank=True, null=True)
    priority_3 = models.CharField(max_length=20, blank=True, null=True)
    priority_4 = models.CharField(max_length=20, blank=True, null=True)
    priority_5 = models.CharField(max_length=20, blank=True, null=True)
    priority_6 = models.CharField(max_length=20, blank=True, null=True)
    followup_private = models.IntegerField(blank=True, null=True)
    task_private = models.IntegerField(blank=True, null=True)
    default_requesttypes_id = models.IntegerField(blank=True, null=True)
    password_forget_token = models.CharField(max_length=40, blank=True, null=True)
    password_forget_token_date = models.DateTimeField(blank=True, null=True)
    user_dn = models.TextField(blank=True, null=True)
    registration_number = models.CharField(max_length=255, blank=True, null=True)
    show_count_on_tabs = models.IntegerField(blank=True, null=True)
    refresh_views = models.IntegerField(blank=True, null=True)
    set_default_tech = models.IntegerField(blank=True, null=True)
    personal_token = models.CharField(max_length=255, blank=True, null=True)
    personal_token_date = models.DateTimeField(blank=True, null=True)
    api_token = models.CharField(max_length=255, blank=True, null=True)
    api_token_date = models.DateTimeField(blank=True, null=True)
    cookie_token = models.CharField(max_length=255, blank=True, null=True)
    cookie_token_date = models.DateTimeField(blank=True, null=True)
    display_count_on_home = models.IntegerField(blank=True, null=True)
    notification_to_myself = models.IntegerField(blank=True, null=True)
    duedateok_color = models.CharField(max_length=255, blank=True, null=True)
    duedatewarning_color = models.CharField(max_length=255, blank=True, null=True)
    duedatecritical_color = models.CharField(max_length=255, blank=True, null=True)
    duedatewarning_less = models.IntegerField(blank=True, null=True)
    duedatecritical_less = models.IntegerField(blank=True, null=True)
    duedatewarning_unit = models.CharField(max_length=255, blank=True, null=True)
    duedatecritical_unit = models.CharField(max_length=255, blank=True, null=True)
    display_options = models.TextField(blank=True, null=True)
    is_deleted_ldap = models.IntegerField()
    pdffont = models.CharField(max_length=255, blank=True, null=True)
    picture = models.CharField(max_length=255, blank=True, null=True)
    begin_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    keep_devices_when_purging_item = models.IntegerField(blank=True, null=True)
    privatebookmarkorder = models.TextField(blank=True, null=True)
    backcreated = models.IntegerField(blank=True, null=True)
    task_state = models.IntegerField(blank=True, null=True)
    layout = models.CharField(max_length=20, blank=True, null=True)
    palette = models.CharField(max_length=20, blank=True, null=True)
    set_default_requester = models.IntegerField(blank=True, null=True)
    lock_autolock_mode = models.IntegerField(blank=True, null=True)
    lock_directunlock_notification = models.IntegerField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    highcontrast_css = models.IntegerField(blank=True, null=True)
    plannings = models.TextField(blank=True, null=True)
    sync_field = models.CharField(max_length=255, blank=True, null=True)
    groups = models.ForeignKey('GlpiGroups', on_delete=models.PROTECT)
    users_id_supervisor = models.IntegerField()
    timezone = models.CharField(max_length=50, blank=True, null=True)
    default_dashboard_central = models.CharField(max_length=100, blank=True, null=True)
    default_dashboard_assets = models.CharField(max_length=100, blank=True, null=True)
    default_dashboard_helpdesk = models.CharField(max_length=100, blank=True, null=True)
    default_dashboard_mini_ticket = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_users'
        unique_together = (('name', 'authtype', 'auths_id'),)


class GlpiUsertitles(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_usertitles'


class GlpiVirtualmachinestates(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    comment = models.TextField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_virtualmachinestates'


class GlpiVirtualmachinesystems(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    comment = models.TextField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_virtualmachinesystems'


class GlpiVirtualmachinetypes(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    comment = models.TextField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_virtualmachinetypes'


class GlpiVlans(models.Model):
    id = models.IntegerField(primary_key=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    tag = models.IntegerField()
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_vlans'


class GlpiVobjects(models.Model):
    id = models.IntegerField(primary_key=True)
    itemtype = models.CharField(max_length=100, blank=True, null=True)
    items_id = models.IntegerField()
    data = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_vobjects'
        unique_together = (('itemtype', 'items_id'),)


class GlpiWifinetworks(models.Model):
    id = models.IntegerField(primary_key=True)
    entities = models.ForeignKey('GlpiEntities', on_delete=models.PROTECT)
    is_recursive = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    essid = models.CharField(max_length=255, blank=True, null=True)
    mode = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glpi_wifinetworks'
