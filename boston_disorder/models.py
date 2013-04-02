from django.db import models
from csvImporter import fields
from csvImporter.model import CsvModel

# Create your models here.
class Crime(models.Model):
    compnos = models.CharField(max_length=200, null=True)
    suppnos = models.CharField(max_length=200, null=True)
    reportingarea = models.CharField(max_length=200, null=True)
    incident_type_description = models.CharField(max_length=200, null=True)
    crime_code = models.CharField(max_length=200, null=True)
    crimecode_description = models.CharField(max_length=200, null=True)
    finalcrimecode = models.CharField(max_length=200, null=True)
    finalcrimecode_desc = models.CharField(max_length=200, null=True)
    reptdistrict = models.CharField(max_length=200, null=True)
    fromdate = models.CharField(max_length=200, null=True)
    todate = models.CharField(max_length=200, null=True)
    weapontype = models.CharField(max_length=200, null=True)
    buildingtype = models.CharField(max_length=200, null=True)
    placeofentry = models.CharField(max_length=200, null=True)
    perpetratorsnos = models.CharField(max_length=200, null=True)
    suspecttransportation = models.CharField(max_length=200, null=True)
    victimactivity = models.CharField(max_length=200, null=True)
    unusualactivity = models.CharField(max_length=200, null=True)
    weather = models.CharField(max_length=200, null=True)
    neighborhood = models.CharField(max_length=200, null=True)
    lighting = models.CharField(max_length=200, null=True)
    clearancestatusdesc = models.CharField(max_length=200, null=True)
    main_crimecode = models.CharField(max_length=200, null=True)
    robbery_type = models.CharField(max_length=200, null=True)
    robbery_attempt = models.CharField(max_length=200, null=True)
    burglary_time = models.CharField(max_length=200, null=True)
    domestic = models.CharField(max_length=200, null=True)
    weapon_type = models.CharField(max_length=200, null=True)
    shift = models.CharField(max_length=200, null=True)
    day_week = models.CharField(max_length=200, null=True)
    ucrpart = models.CharField(max_length=200, null=True)
    location = models.CharField(max_length=200, null=True)
    x = models.CharField(max_length=200, null=True)
    y = models.CharField(max_length=200, null=True)
    score = models.CharField(max_length=200, null=True)
    greporting = models.CharField(max_length=200, null=True)
    gsector = models.CharField(max_length=200, null=True)
    gbeat = models.CharField(max_length=200, null=True)
    gdistrict = models.CharField(max_length=200, null=True)
    shooting_type = models.CharField(max_length=200, null=True)
    computedcrimecode = models.CharField(max_length=200, null=True)
    computedcrimedesc = models.CharField(max_length=200, null=True)
    location_1 = models.CharField(max_length=200, null=True)

class ServiceRequest(models.Model):
    case_enquiry_id = models.CharField(max_length=200, null=True)
    open_dt = models.CharField(max_length=200, null=True)
    closed_dt = models.CharField(max_length=200, null=True)
    case_status = models.CharField(max_length=200, null=True)
    closure_reason = models.CharField(max_length=200, null=True)
    case_title = models.CharField(max_length=200, null=True)
    subject = models.CharField(max_length=200, null=True)
    reason = models.CharField(max_length=200, null=True)
    type = models.CharField(max_length=200, null=True)
    queue = models.CharField(max_length=200, null=True)
    department = models.CharField(max_length=200, null=True)
    location = models.CharField(max_length=200, null=True)
    fire_district = models.CharField(max_length=200, null=True)
    pwd_district = models.CharField(max_length=200, null=True)
    city_council_district = models.CharField(max_length=200, null=True)
    police_district = models.CharField(max_length=200, null=True)
    neighborhood = models.CharField(max_length=200, null=True)
    neighborhood_services_district = models.CharField(max_length=200, null=True)
    ward = models.CharField(max_length=200, null=True)
    precinct = models.CharField(max_length=200, null=True)
    land_usage = models.CharField(max_length=200, null=True)
    location_street_name = models.CharField(max_length=200, null=True)
    location_zipcode = models.CharField(max_length=200, null=True)
    location_x = models.CharField(max_length=200, null=True)
    location_y = models.CharField(max_length=200, null=True)
    source = models.CharField(max_length=200, null=True)
    geocoded_loc = models.CharField(max_length=200, null=True)

class InspectionViolation(models.Model):
    casenumber = models.CharField(max_length=200, null=True)#models.CharField(max_length=200, null=True)
    ticketnumber = models.CharField(max_length=200, null=True)#models.CharField(max_length=200, null=True)
    violationdate = models.CharField(max_length=200, null=True)#models.CharField(max_length=200, null=True)
    result = models.CharField(max_length=200, null=True)#models.CharField(max_length=200, null=True)
    caseinfostatus = models.CharField(max_length=200, null=True)#models.CharField(max_length=200, null=True)
    amt = models.CharField(max_length=200, null=True)#models.CharField(max_length=200, null=True)
    stat = models.CharField(max_length=200, null=True)#models.CharField(max_length=200, null=True)
    namefirst = models.CharField(max_length=200, null=True)#models.CharField(max_length=200, null=True)
    namelast = models.CharField(max_length=200, null=True)#models.CharField(max_length=200, null=True)
    addressid = models.CharField(max_length=200, null=True)#models.CharField(max_length=200, null=True)
    ward = models.CharField(max_length=200, null=True)#models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)#models.CharField(max_length=200, null=True)
    suffix = models.CharField(max_length=200, null=True)#models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)#models.CharField(max_length=200, null=True)
    stname = models.CharField(max_length=200, null=True)#models.CharField(max_length=200, null=True)
    stno = models.CharField(max_length=200, null=True)#models.CharField(max_length=200, null=True)
    stnohi = models.CharField(max_length=200, null=True)#models.CharField(max_length=200, null=True)
    zip = models.CharField(max_length=200, null=True)#models.CharField(max_length=200, null=True)
    gpsy = models.CharField(max_length=200, null=True)#models.DecimalField(decimal_places=4, null=True)
    gpsx = models.CharField(max_length=200, null=True)#models.DecimalField(decimal_places=4, null=True)
    addrkey = models.CharField(max_length=200, null=True)#models.CharField(max_length=200, null=True)
    feelastmoddte = models.CharField(max_length=200, null=True)#models.CharField(max_length=200, null=True)
    pri = models.CharField(max_length=200, null=True)#models.CharField(max_length=200, null=True)
    failedcode = models.CharField(max_length=200, null=True)#models.CharField(max_length=200, null=True)
    descript = models.CharField(max_length=200, null=True)#models.CharField(max_length=200, null=True)
    paiddttm = models.CharField(max_length=200, null=True)#models.CharField(max_length=200, null=True)
    waived = models.CharField(max_length=200, null=True)#models.CharField(max_length=200, null=True)
    liened = models.CharField(max_length=200, null=True)#models.CharField(max_length=200, null=True)
    comments = models.CharField(max_length=200, null=True)#models.CharField(max_length=200, null=True)

class CAD(models.Model):
    inc_no = models.CharField(max_length=200, null=True)
    inf_addr = models.CharField(max_length=200, null=True)
    address_text = models.CharField(max_length=200, null=True)
    matched = models.CharField(max_length=200, null=True)
    match_score = models.CharField(max_length=200, null=True)#models.IntegerField(null=True)
    match_test = models.CharField(max_length=200, null=True)
    match_type = models.CharField(max_length=200, null=True)
    match_id = models.CharField(max_length=200, null=True)#models.IntegerField(max_length=200, null=True)
    matchxcoordinate = models.CharField(max_length=200, null=True)#models.DecimalField(decimal_places=4, null=True)
    matchycoordinate = models.CharField(max_length=200, null=True)#models.DecimalField(decimal_places=3, null=True)
    match_codes = models.CharField(max_length=200, null=True)
    propid = models.CharField(max_length=200, null=True)
    final_type = models.CharField(max_length=200, null=True)
    priority = models.CharField(max_length=200, null=True)#models.IntegerField(max_length=200, null=True)
    close_dt = models.CharField(max_length=200, null=True)
    type_desc = models.CharField(max_length=200, null=True)
    disorder = models.CharField(max_length=200, null=True)#models.BooleanField(null=True)
    medemerg = models.CharField(max_length=200, null=True)#models.BooleanField(null=True)
    violent = models.CharField(max_length=200, null=True)#models.BooleanField(null=True)

class Fire(models.Model):
    status = models.CharField(max_length=200, null=True)
    score = models.CharField(max_length=200, null=True)#models.DecimalField(decimal_places=2, null=True)
    match_type = models.CharField(max_length=200, null=True)
    match_addr = models.CharField(max_length=200, null=True)
    side = models.CharField(max_length=200, null=True)
    ref_id = models.CharField(max_length=200, null=True)#models.IntegerField(null=True)
    x = models.CharField(max_length=200, null=True)#models.DecimalField(decimal_places=6, null=True)
    y = models.CharField(max_length=200, null=True)#models.DecimalField(decimal_places=6, null=True)
    user_fld = models.CharField(max_length=200, null=True)#models.IntegerField(null=True)
    addr_type = models.CharField(max_length=200, null=True)
    arc_street = models.CharField(max_length=200, null=True)
    arc_zip = models.CharField(max_length=200, null=True)#models.IntegerField(null=True)
    inci_no = models.CharField(max_length=200, null=True)
    aim_date = models.CharField(max_length=200, null=True)
    aim_time = models.CharField(max_length=200, null=True)
    inci_type = models.CharField(max_length=200, null=True)#models.IntegerField(null=True)
    descript = models.CharField(max_length=200,null=True)
    prop_loss = models.CharField(max_length=200, null=True)#models.IntegerField(null=True)
    cont_loss = models.CharField(max_length=200, null=True)#models.IntegerField(null=True)
    aim_type = models.CharField(max_length=200, null=True)#models.IntegerField(null=True)
    district = models.CharField(max_length=200, null=True)#models.IntegerField(null=True)
    cause_ign = models.CharField(max_length=200, null=True)#models.IntegerField(null=True)
    descript_b = models.CharField(max_length=200, null=True)
    addr_typ_1 = models.CharField(max_length=200,null=True)
    number = models.CharField(max_length=200, null=True)#models.IntegerField(null=True)
    st_prefix = models.CharField(max_length=200,null=True)
    street = models.CharField(max_length=200,null=True)
    st_type = models.CharField(max_length=200,null=True)
    addr_2 = models.CharField(max_length=200,null=True)
    apt_room = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zip = models.CharField(max_length=200, null=True)#models.IntegerField(null=True)
    how_receiv = models.CharField(max_length=200, null=True)
    total_loss = models.CharField(max_length=200, null=True)#models.IntegerField(null=True)
    address = models.CharField(max_length=200,null=True)
    address_zip = models.CharField(max_length=200,null=True)
    locationid = models.CharField(max_length=200, null=True)#models.IntegerField(null=True)

class HansonPermits(models.Model):
    apbldkey = models.CharField(max_length=200, null=True)
    permittype = models.CharField(max_length=200, null=True)
    adddttm = models.CharField(max_length=200, null=True)
    moddttm = models.CharField(max_length=200, null=True)
    expdttm = models.CharField(max_length=200, null=True)
    permitstatus = models.CharField(max_length=200, null=True)
    worktype = models.CharField(max_length=200, null=True)
    permitnumber = models.CharField(max_length=200, null=True)
    addrkey = models.CharField(max_length=200, null=True)
    block = models.CharField(max_length=200, null=True)
    ward = models.CharField(max_length=200, null=True)
    predir = models.CharField(max_length=200, null=True)
    stno = models.CharField(max_length=200, null=True)
    stnohi = models.CharField(max_length=200, null=True)
    stname = models.CharField(max_length=200, null=True)
    suffix = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    zip = models.CharField(max_length=200, null=True)
    gpsy = models.CharField(max_length=200, null=True)
    gpsx = models.CharField(max_length=200, null=True)
    issdttm = models.CharField(max_length=200, null=True)
    pri = models.CharField(max_length=200, null=True)
    occupancytype = models.CharField(max_length=200, null=True)
    coodttm = models.CharField(max_length=200, null=True)
    tmpcoodttm = models.CharField(max_length=200, null=True)
    permittypedescr = models.CharField(max_length=200, null=True)
    bldgarea = models.CharField(max_length=200, null=True)
    finaldttm = models.CharField(max_length=200, null=True)
    descript = models.CharField(max_length=200, null=True)

class CRM(models.Model):
    case_enquiry_id = models.CharField(max_length=200, null=True) #int
    case_reference = models.CharField(max_length=200, null=True) #int
    open_dt = models.CharField(max_length=200, null=True) #date
    close_dt = models.CharField(max_length=200, null=True) #date
    subject = models.CharField(max_length=200, null=True)
    reason = models.CharField(max_length=200, null=True)
    type = models.CharField(max_length=200, null=True)
    case_x = models.CharField(max_length=200, null=True) #float
    case_y = models.CharField(max_length=200, null=True) #float
    location = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    propid = models.CharField(max_length=200, null=True)
    parcel_num = models.CharField(max_length=200, null=True)
    neighborhood = models.CharField(max_length=200, null=True)
    channel_type = models.CharField(max_length=200, null=True)
    party_id = models.CharField(max_length=200, null=True) #int
    source = models.CharField(max_length=200, null=True)
    locationid = models.CharField(max_length=200, null=True) #int
    ref_id = models.CharField(max_length=200, null=True) #int
    x = models.CharField(max_length=200, null=True) #float
    y = models.CharField(max_length=200, null=True) #float
    landuse = models.CharField(max_length=200, null=True)
    blk_id = models.CharField(max_length=200, null=True)#int
    bg_id = models.CharField(max_length=200, null=True)#int
    ct_id = models.CharField(max_length=200, null=True)#int
    nbhd = models.CharField(max_length=200, null=True)
    nsa_name = models.CharField(max_length=200, null=True)
    objectid = models.CharField(max_length=200, null=True)#int
    #code = models.CharField(max_length=200, null=True) #int
    public = models.CharField(max_length=200, null=True)
    unciviluse = models.CharField(max_length=200, null=True)#bool
    housing = models.CharField(max_length=200, null=True)#bool
    bigbuild = models.CharField(max_length=200, null=True)#bool
    graffiti = models.CharField(max_length=200, null=True)#bool
    trash = models.CharField(max_length=200, null=True)#bool
    privateneglect = models.CharField(max_length=200, null=True)#bool
    problem = models.CharField(max_length=200, null=True)#bool
    publicdenig = models.CharField(max_length=200, null=True)#bool
    my = models.CharField(max_length=200, null=True)#bool
    bg = models.CharField(max_length=200, null=True)#bool

class BlockGroup(models.Model):
    objectid = models.CharField(max_length=200, null=True) #int
    area = models.CharField(max_length=200, null=True) #float
    perimeter = models.CharField(max_length=200, null=True) #float
    state =  models.CharField(max_length=200, null=True) #int
    county = models.CharField(max_length=200, null=True) #int
    tract = models.CharField(max_length=200, null=True) #int
    blockgroup = models.CharField(max_length=200, null=True) #int
    bg_id = models.CharField(max_length=200, null=True) #int
    ct_id = models.CharField(max_length=200, null=True) #int
    blk_count = models.CharField(max_length=200, null=True) #int
    logrecno = models.CharField(max_length=200, null=True) #int
    dry_acres = models.CharField(max_length=200, null=True) #float
    dry_sqmi = models.CharField(max_length=200, null=True) #float
    dry_sqkm = models.CharField(max_length=200, null=True) #float
    shape_area = models.CharField(max_length=200, null=True) #float
    shape_len = models.CharField(max_length=200, null=True) #float
    hoods_pd = models.CharField(max_length=200, null=True) #float
    nbhd = models.CharField(max_length=200, null=True) 
    nbhdCRM = models.CharField(max_length=200, null=True)
    nsa_id = models.CharField(max_length=200, null=True) #int
    nsa_name = models.CharField(max_length=200, null=True) #int
    bg_id_1 = models.CharField(max_length=200, null=True) #float
    homeowners = models.CharField(max_length=200, null=True) #float
    medincome = models.CharField(max_length=200, null=True) #float
    propwhite = models.CharField(max_length=200, null=True) #float
    propblack = models.CharField(max_length=200, null=True) #float
    propasian = models.CharField(max_length=200, null=True) #float
    prophisp = models.CharField(max_length=200, null=True) #float
    medage = models.CharField(max_length=200, null=True) #float
    propcollege = models.CharField(max_length=200, null=True) #float
    totalpop = models.CharField(max_length=200, null=True) #float
    popden = models.CharField(max_length=200, null=True) #float

class Calls(models.Model):
    inc_no = models.CharField(max_length=200, null=True)
    inf_addr = models.CharField(max_length=200, null=True)
    address_text = models.CharField(max_length=200, null=True)
    matched = models.CharField(max_length=200, null=True)
    match_score = models.CharField(max_length=200, null=True)
    match_test = models.CharField(max_length=200, null=True)
    match_type = models.CharField(max_length=200, null=True)
    match_id = models.CharField(max_length=200, null=True)
    matchxcoordinate = models.CharField(max_length=200, null=True)
    matchycoordinate = models.CharField(max_length=200, null=True)
    match_codes = models.CharField(max_length=200, null=True)
    propid = models.CharField(max_length=200, null=True)
    final_type = models.CharField(max_length=200, null=True)
    priority = models.CharField(max_length=200, null=True)
    close_dt = models.CharField(max_length=200, null=True)
    type_desc = models.CharField(max_length=200, null=True)
    disorder = models.CharField(max_length=200, null=True)
    medemerg = models.CharField(max_length=200, null=True)
    violent = models.CharField(max_length=200, null=True)
    locationid = models.CharField(max_length=200, null=True)
    ref_id = models.CharField(max_length=200, null=True)
    x = models.CharField(max_length=200, null=True)
    y = models.CharField(max_length=200, null=True)
    landuse = models.CharField(max_length=200, null=True)
    blk_id = models.CharField(max_length=200, null=True)
    bg_id = models.CharField(max_length=200, null=True)
    ct_id = models.CharField(max_length=200, null=True)
    nbhd = models.CharField(max_length=200, null=True)
    nsa_name = models.CharField(max_length=200, null=True)
    objectid = models.CharField(max_length=200, null=True)
    medemerg1 = models.CharField(max_length=200, null=True)
    respobgyn = models.CharField(max_length=200, null=True)
    medemerg_gnrl = models.CharField(max_length=200, null=True)
    socdis = models.CharField(max_length=200, null=True)
    socstrife = models.CharField(max_length=200, null=True)
    alcohol = models.CharField(max_length=200, null=True)
    violence = models.CharField(max_length=200, null=True)
    guns = models.CharField(max_length=200, null=True)
    homeinv = models.CharField(max_length=200, null=True)

class AddressLatLog(models.Model):
    address = models.CharField(max_length=200, null=True)
    latitude = models.CharField(max_length=200, null=True)
    longitude = models.CharField(max_length=200, null=True)

class TigerData(models.Model):
    type = models.CharField(max_length=200, null=True)
    areaid = models.CharField(max_length=200, null=True)
    latitude = models.CharField(max_length=200, null=True)
    longitude = models.CharField(max_length=200, null=True)
    
#my_csv_list = CSVInspectionViolation.import_data(data = open("study_18864/Data/Database/InspectionViolations.csv"))
class CSVInspectionViolation(CsvModel):
    casenumber = fields.CharField()
    ticketnumber = fields.CharField()
    violationdate = fields.CharField()
    result = fields.CharField()
    caseinfostatus = fields.CharField()
    amt = fields.CharField()
    stat = fields.CharField()
    namefirst = fields.CharField()
    namelast = fields.CharField()
    addressid = fields.CharField()
    ward = fields.CharField()
    city = fields.CharField()
    suffix = fields.CharField()
    state = fields.CharField()
    stname = fields.CharField()
    stno = fields.CharField()
    stnohi = fields.CharField()
    zip = fields.CharField()
    gpsy = fields.CharField()#fields.FloatField()
    gpsx = fields.CharField()#fields.FloatField()
    addrkey = fields.CharField()
    feelastmoddte = fields.CharField()
    pri = fields.CharField()
    failedcode = fields.CharField()
    descript = fields.CharField()
    paiddttm = fields.CharField()
    waived = fields.CharField()
    liened = fields.CharField()
    comments = fields.CharField()

    class Meta:
        delimiter = ","
        dbModel = InspectionViolation

class CSVCAD(CsvModel):
    inc_no = fields.CharField()
    inf_addr = fields.CharField()
    address_text = fields.CharField()
    matched = fields.CharField()
    match_score = fields.CharField()#fields.IntegerField()
    match_test = fields.CharField()
    match_type = fields.CharField()
    match_id = fields.CharField()#fields.IntegerField()
    matchxcoordinate = fields.CharField()#fields.FloatField()
    matchycoordinate = fields.CharField()#fields.FloatField()
    match_codes = fields.CharField()
    propid = fields.CharField()
    final_type = fields.CharField()
    priority = fields.CharField()#fields.IntegerField()
    close_dt = fields.CharField()
    type_desc = fields.CharField()
    disorder = fields.CharField()#fields.BooleanField()
    medemerg = fields.CharField()#fields.BooleanField()
    violent = fields.CharField()#fields.BooleanField()

    class Meta:
        delimiter = ","
        dbModel = CAD
#my_csv_list = CSVFire.import_data(data = open("FiresFinal.csv"))
class CSVFire(CsvModel):
    status = fields.CharField()
    score = fields.CharField()
    match_type = fields.CharField()
    match_addr = fields.CharField()
    side = fields.CharField()
    ref_id = fields.CharField()
    x = fields.CharField()
    y = fields.CharField()
    user_fld = fields.CharField()
    addr_type = fields.CharField()
    arc_street = fields.CharField()
    arc_zip = fields.CharField()
    inci_no = fields.CharField()
    aim_date = fields.CharField()
    aim_time = fields.CharField()
    inci_type = fields.CharField()
    descript = fields.CharField()
    prop_loss = fields.CharField()
    cont_loss = fields.CharField()
    aim_type = fields.CharField()
    district = fields.CharField()
    cause_ign = fields.CharField()
    descript_b = fields.CharField()
    addr_typ_1 = fields.CharField()
    number = fields.CharField()
    st_prefix = fields.CharField()
    street = fields.CharField()
    st_type = fields.CharField()
    addr_2 = fields.CharField()
    apt_room = fields.CharField()
    city = fields.CharField()
    state = fields.CharField()
    zip = fields.CharField()
    how_receiv = fields.CharField()
    total_loss = fields.CharField()
    address = fields.CharField()
    address_zip = fields.CharField()
    locationid = fields.CharField()

    class Meta:
        delimiter = ","
        dbModel = Fire

class CSVHansonPermits(CsvModel):
    apbldkey = fields.CharField()
    permittype = fields.CharField()
    adddttm = fields.CharField()
    moddttm = fields.CharField()
    expdttm = fields.CharField()
    permitstatus = fields.CharField()
    worktype = fields.CharField()
    permitnumber = fields.CharField()
    addrkey = fields.CharField()
    block = fields.CharField()
    ward = fields.CharField()
    predir = fields.CharField()
    stno = fields.CharField()
    stnohi = fields.CharField()
    stname = fields.CharField()
    suffix = fields.CharField()
    city = fields.CharField()
    zip = fields.CharField()
    gpsy = fields.CharField()
    gpsx = fields.CharField()
    issdttm = fields.CharField()
    pri = fields.CharField()
    occupancytype = fields.CharField()
    coodttm = fields.CharField()
    tmpcoodttm = fields.CharField()
    permittypedescr = fields.CharField()
    bldgarea = fields.CharField()
    finaldttm = fields.CharField()
    descript = fields.CharField()

    class Meta:
        delimiter = ","
        dbModel = HansonPermits

class CSVCRM(CsvModel):
    case_enquiry_id = fields.CharField() #int
    case_reference = fields.CharField() #int
    open_dt = fields.CharField() #date
    close_dt = fields.CharField() #date
    subject = fields.CharField()
    reason = fields.CharField()
    type = fields.CharField()
    case_x = fields.CharField() #float
    case_y = fields.CharField() #float
    location = fields.CharField()
    city = fields.CharField()
    state = fields.CharField()
    propid = fields.CharField()
    parcel_num = fields.CharField()
    neighborhood = fields.CharField()
    channel_type = fields.CharField()
    party_id = fields.CharField() #int
    source = fields.CharField()
    locationid = fields.CharField() #int
    ref_id = fields.CharField() #int
    x = fields.CharField() #float
    y = fields.CharField() #float
    landuse = fields.CharField()
    blk_id = fields.CharField()#int
    bg_id = fields.CharField()#int
    ct_id = fields.CharField()#int
    nbhd = fields.CharField()
    nsa_name = fields.CharField()
    objectid = fields.CharField()#int
    #code = fields.CharField() #int
    public = fields.CharField()#bool
    unciviluse = fields.CharField()#bool
    housing = fields.CharField()#bool
    bigbuild = fields.CharField()#bool
    graffiti = fields.CharField()#bool
    trash = fields.CharField()#bool
    privateneglect = fields.CharField()#bool
    problem = fields.CharField()#bool
    publicdenig = fields.CharField()#bool
    my = fields.CharField()
    bg = fields.CharField()

    class Meta:
        delimiter = ","
        dbModel = CRM

class CSVBlockGroup(CsvModel):
    objectid = fields.CharField() #int
    area = fields.CharField() #float
    perimeter = fields.CharField() #float
    state = fields.CharField() #int
    county = fields.CharField() #int
    tract = fields.CharField() #int
    blockgroup = fields.CharField() #int
    bg_id = fields.CharField() #int
    ct_id = fields.CharField() #int
    blk_count = fields.CharField() #int
    logrecno = fields.CharField() #int
    dry_acres = fields.CharField() #float
    dry_sqmi = fields.CharField() #float
    dry_sqkm = fields.CharField() #float
    shape_area = fields.CharField() #float
    shape_len = fields.CharField() #float
    hoods_pd = fields.CharField() #float
    nbhd = fields.CharField() 
    nbhdCRM = fields.CharField()
    nsa_id = fields.CharField() #int
    nsa_name = fields.CharField() #int
    bg_id_1 = fields.CharField() #float
    homeowners = fields.CharField() #float
    medincome = fields.CharField() #float
    propwhite = fields.CharField() #float
    propblack = fields.CharField() #float
    propasian = fields.CharField() #float
    prophisp = fields.CharField() #float
    medage = fields.CharField() #float
    propcollege = fields.CharField() #float
    totalpop = fields.CharField() #float
    popden = fields.CharField() #float

    class Meta:
        delimiter = ","
        dbModel = BlockGroup

class CSVTigerData(CsvModel):
    type = fields.CharField()
    areaid = fields.CharField()
    latitude = fields.CharField()
    longitude = fields.CharField()

    class Meta:
        delimiter = ","
        dbModel = TigerData

class CSV911Calls(CsvModel):
    inc_no = fields.CharField()
    inf_addr = fields.CharField()
    address_text = fields.CharField()
    matched = fields.CharField()
    match_score = fields.CharField()
    match_test = fields.CharField()
    match_type = fields.CharField()
    match_id = fields.CharField()
    matchxcoordinate = fields.CharField()
    matchycoordinate = fields.CharField()
    match_codes = fields.CharField()
    propid = fields.CharField()
    final_type = fields.CharField()
    priority = fields.CharField()
    close_dt = fields.CharField()
    type_desc = fields.CharField()
    disorder = fields.CharField()
    medemerg = fields.CharField()
    violent = fields.CharField()
    locationid = fields.CharField()
    ref_id = fields.CharField()
    x = fields.CharField()
    y = fields.CharField()
    landuse = fields.CharField()
    blk_id = fields.CharField()
    bg_id = fields.CharField()
    ct_id = fields.CharField()
    nbhd = fields.CharField()
    nsa_name = fields.CharField()
    objectid = fields.CharField()
    medemerg1 = fields.CharField()
    respobgyn = fields.CharField()
    medemerg_gnrl = fields.CharField()
    socdis = fields.CharField()
    socstrife = fields.CharField()
    alcohol = fields.CharField()
    violence = fields.CharField()
    guns = fields.CharField()
    homeinv = fields.CharField()

    class Meta:
        delimiter = ","
        dbModel = Calls

class BostonInspectionViolation(models.Model):
    casenumber = models.CharField(max_length=200, null=True)
    ticketnumber = models.CharField(max_length=200, null=True)
    violationdate = models.DateField(null=True)
    result = models.CharField(max_length=200, null=True)
    caseinfostatus = models.CharField(max_length=200, null=True)
    amt = models.IntegerField(null=True)
    stat = models.CharField(max_length=200, null=True)
    namefirst = models.CharField(max_length=200, null=True)
    namelast = models.CharField(max_length=200, null=True)
    addressid = models.IntegerField(null=True)
    ward = models.IntegerField(null=True)
    city = models.CharField(max_length=200, null=True)
    suffix = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    stname = models.CharField(max_length=200, null=True)
    stno = models.IntegerField(null=True)
    stnohi = models.IntegerField(null=True)
    zip = models.IntegerField(null=True)
    gpsy = models.FloatField(null=True)
    gpsx = models.FloatField(null=True)
    addrkey = models.CharField(max_length=200, null=True)
    feelastmoddte = models.IntegerField(null=True)
    pri = models.CharField(max_length=200, null=True)
    failedcode = models.IntegerField(null=True)
    descript = models.CharField(max_length=200, null=True)
    paiddttm = models.CharField(max_length=200, null=True)
    waived = models.CharField(max_length=200, null=True)
    liened = models.CharField(max_length=200, null=True)
    comments = models.CharField(max_length=200, null=True)

class BostonCAD(models.Model):
    inc_no = models.CharField(max_length=200, null=True)
    inf_addr = models.CharField(max_length=200, null=True)
    address_text = models.CharField(max_length=200, null=True)
    matched = models.CharField(max_length=200, null=True)
    match_score = models.IntegerField(null=True)
    match_test = models.CharField(max_length=200, null=True)
    match_type = models.CharField(max_length=200, null=True)
    match_id = models.IntegerField(null=True)
    matchxcoordinate = models.FloatField(null=True)
    matchycoordinate = models.FloatField(null=True)
    match_codes = models.CharField(max_length=200, null=True)
    propid = models.CharField(max_length=200, null=True)
    final_type = models.CharField(max_length=200, null=True)
    priority = models.IntegerField(null=True)
    close_dt = models.DateField(null=True)
    type_desc = models.CharField(max_length=200, null=True)
    disorder = models.BooleanField(default=False)
    medemerg = models.BooleanField(default=False)
    violent = models.BooleanField(default=False)

class BostonFire(models.Model):
    status = models.CharField(max_length=200, null=True)
    score = models.FloatField(null=True)
    match_type = models.CharField(max_length=200, null=True)
    match_addr = models.CharField(max_length=200, null=True)
    side = models.CharField(max_length=200, null=True)
    ref_id = models.IntegerField(null=True)
    x = models.FloatField(null=True)
    y = models.FloatField(null=True)
    user_fld = models.IntegerField(null=True)
    addr_type = models.CharField(max_length=200, null=True)
    arc_street = models.CharField(max_length=200, null=True)
    arc_zip = models.IntegerField(null=True)
    inci_no = models.CharField(max_length=200, null=True)
    aim_date = models.DateField(null=True)
    aim_time = models.DateField(null=True)
    inci_type = models.IntegerField(null=True)
    descript = models.CharField(max_length=200,null=True)
    prop_loss = models.IntegerField(null=True)
    cont_loss = models.IntegerField(null=True)
    aim_type = models.IntegerField(null=True)
    district = models.IntegerField(null=True)
    cause_ign = models.IntegerField(null=True)
    descript_b = models.CharField(max_length=200, null=True)
    addr_typ_1 = models.CharField(max_length=200,null=True)
    number = models.IntegerField(null=True)
    st_prefix = models.CharField(max_length=200,null=True)
    street = models.CharField(max_length=200,null=True)
    st_type = models.CharField(max_length=200,null=True)
    addr_2 = models.CharField(max_length=200,null=True)
    apt_room = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zip = models.IntegerField(null=True)
    how_receiv = models.CharField(max_length=200, null=True)
    total_loss = models.IntegerField(null=True)
    address = models.CharField(max_length=200,null=True)
    address_zip = models.CharField(max_length=200,null=True)
    locationid = models.IntegerField(null=True)

class BostonPermits(models.Model):
    apbldkey = models.IntegerField(null=True)
    permittype = models.CharField(max_length=200, null=True)
    adddttm = models.CharField(max_length=200, null=True)
    moddttm = models.CharField(max_length=200, null=True)
    expdttm = models.CharField(max_length=200, null=True)
    permitstatus = models.CharField(max_length=200, null=True)
    worktype = models.CharField(max_length=200, null=True)
    permitnumber = models.CharField(max_length=200, null=True)
    addrkey = models.IntegerField(null=True)
    block = models.CharField(max_length=200, null=True)
    ward = models.IntegerField(null=True)
    predir = models.CharField(max_length=200, null=True)
    stno = models.CharField(max_length=200, null=True)
    stnohi = models.CharField(max_length=200, null=True)
    stname = models.CharField(max_length=200, null=True)
    suffix = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    zip = models.IntegerField(null=True)
    gpsy = models.FloatField(null=True)
    gpsx = models.FloatField(null=True)
    issdttm = models.CharField(max_length=200, null=True)
    pri = models.CharField(max_length=200, null=True)
    occupancytype = models.CharField(max_length=200, null=True)
    coodttm = models.CharField(max_length=200, null=True)
    tmpcoodttm = models.CharField(max_length=200, null=True)
    permittypedescr = models.CharField(max_length=200, null=True)
    bldgarea = models.FloatField(null=True)
    finaldttm = models.CharField(max_length=200, null=True)
    descript = models.CharField(max_length=200, null=True)

class BostonCRM(models.Model):
    case_enquiry_id = models.IntegerField(null=True) #int
    case_reference = models.IntegerField(null=True) #int
    open_dt = models.DateField(null=True) #date
    close_dt = models.DateField(null=True) #date
    subject = models.CharField(max_length=200, null=True)
    reason = models.CharField(max_length=200, null=True)
    type = models.CharField(max_length=200, null=True)
    case_x = models.FloatField(null=True) #float
    case_y = models.FloatField(null=True) #float
    location = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    propid = models.CharField(max_length=200, null=True)
    parcel_num = models.CharField(max_length=200, null=True)
    neighborhood = models.CharField(max_length=200, null=True)
    channel_type = models.CharField(max_length=200, null=True)
    party_id = models.IntegerField(null=True) #int
    source = models.CharField(max_length=200, null=True)
    locationid = models.IntegerField(null=True) #int
    ref_id = models.IntegerField(null=True) #int
    x = models.FloatField(null=True) #float
    y = models.FloatField(null=True) #float
    landuse = models.CharField(max_length=200, null=True)
    blk_id = models.IntegerField(null=True)#int
    bg_id = models.IntegerField(null=True)#int
    ct_id = models.IntegerField(null=True)#int
    nbhd = models.CharField(max_length=200, null=True)
    nsa_name = models.CharField(max_length=200, null=True)
    objectid = models.IntegerField(null=True)#int
    #code = models.IntegerField(null=True) #int
    public = models.BooleanField(default=False)#bool
    unciviluse = models.BooleanField(default=False)#bool
    housing = models.BooleanField(default=False)#bool
    bigbuild = models.BooleanField(default=False)#bool
    graffiti = models.BooleanField(default=False)#bool
    trash = models.BooleanField(default=False)#bool
    privateneglect = models.BooleanField(default=False)#bool
    problem = models.BooleanField(default=False)#bool
    publicdenig = models.BooleanField(default=False)#bool
    my = models.IntegerField(null=True) #int
    bg = models.BooleanField(default=False)#bool

class BostonBlockGroup(models.Model):
    objectid = models.IntegerField(null=True) #int
    area = models.FloatField(null=True)
    perimeter = models.FloatField(null=True)
    state = models.IntegerField(null=True)
    county = models.IntegerField(null=True)
    tract = models.IntegerField(null=True)
    blockgroup = models.IntegerField(null=True)
    bg_id = models.IntegerField(null=True)
    ct_id = models.IntegerField(null=True)
    blk_count = models.IntegerField(null=True)
    logrecno = models.IntegerField(null=True)
    dry_acres = models.FloatField(null=True)
    dry_sqmi = models.FloatField(null=True)
    dry_sqkm = models.FloatField(null=True)
    shape_area = models.FloatField(null=True)
    shape_len = models.FloatField(null=True)
    hoods_pd = models.FloatField(null=True)
    nbhd = models.CharField(max_length=200, null=True) 
    nbhdCRM = models.CharField(max_length=200, null=True)
    nsa_id = models.CharField(max_length=200, null=True)
    nsa_name = models.CharField(max_length=200, null=True)
    bg_id_1 = models.FloatField(null=True)
    homeowners = models.FloatField(null=True)
    medincome = models.FloatField(null=True)
    propwhite = models.FloatField(null=True)
    propblack = models.FloatField(null=True)
    propasian = models.FloatField(null=True)
    prophisp = models.FloatField(null=True)
    medage = models.FloatField(null=True)
    propcollege = models.FloatField(null=True)
    totalpop = models.FloatField(null=True)
    popden = models.FloatField(null=True)

class Boston911Calls(models.Model):
    inc_no = models.CharField(max_length=200, null=True)
    inf_addr = models.CharField(max_length=200, null=True)
    address_text = models.CharField(max_length=200, null=True)
    matched = models.CharField(max_length=200, null=True)
    match_score = models.IntegerField(null=True)
    match_test = models.CharField(max_length=200, null=True)
    match_type = models.CharField(max_length=200, null=True)
    match_id = models.IntegerField(null=True)
    matchxcoordinate = models.FloatField(null=True)
    matchycoordinate = models.FloatField(null=True)
    match_codes = models.CharField(max_length=200, null=True)
    propid = models.CharField(max_length=200, null=True)
    final_type = models.CharField(max_length=200, null=True)
    priority = models.IntegerField(null=True)
    close_dt = models.DateField(null=True)
    type_desc = models.CharField(max_length=200, null=True)
    disorder = models.BooleanField(default=False)
    medemerg = models.BooleanField(default=False)
    violent = models.BooleanField(default=False)
    locationid = models.IntegerField(null=True)
    ref_id = models.IntegerField(null=True)
    x = models.FloatField(null=True)
    y = models.FloatField(null=True)
    landuse = models.CharField(max_length=200, null=True)
    blk_id = models.IntegerField(null=True)
    bg_id = models.IntegerField(null=True)
    ct_id = models.IntegerField(null=True)
    nbhd = models.CharField(max_length=200, null=True) 
    nsa_name = models.CharField(max_length=200, null=True)
    objectid = models.CharField(max_length=200, null=True)
    medemerg1 = models.BooleanField(default=False)
    respobgyn = models.BooleanField(default=False)
    medemerg_gnrl = models.BooleanField(default=False)
    socdis = models.BooleanField(default=False)
    socstrife = models.BooleanField(default=False)
    alcohol = models.BooleanField(default=False)
    violence = models.BooleanField(default=False)
    guns = models.BooleanField(default=False)
    homeinv = models.BooleanField(default=False)


