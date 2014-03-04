from django.db import models
from csvImporter import fields
from csvImporter.model import CsvModel


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
    propid = models.CharField(max_length=200, null=True)
    parcel_num = models.CharField(max_length=200, null=True)
    neighborhood = models.CharField(max_length=200, null=True)
    location_zip = models.CharField(max_length=200, null=True)
    channel_type = models.CharField(max_length=200, null=True)
    reporter_city = models.CharField(max_length=200, null=True)
    reporter_zip = models.CharField(max_length=200, null=True)
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
    sam_id = models.CharField(max_length=200, null=True)
    prop_type = models.CharField(max_length=200, null=True)
    disp_grp = models.CharField(max_length=200, null=True)
    type = models.CharField(max_length=200, null=True)
    priority = models.CharField(max_length=200, null=True)
    close_dt = models.CharField(max_length=200, null=True)
    entry_dt = models.CharField(max_length=200, null=True)
    disp_dt = models.CharField(max_length=200, null=True)
    enrte_dt = models.CharField(max_length=200, null=True)
    onscene_dt = models.CharField(max_length=200, null=True)
    recieve_dt = models.CharField(max_length=200, null=True)
    all_wait_tm = models.CharField(max_length=200, null=True)
    all_entre_tm = models.CharField(max_length=200, null=True)
    all_onscene_tm = models.CharField(max_length=200, null=True)
    all_dsip_tm = models.CharField(max_length=200, null=True)
    comp_src = models.CharField(max_length=200, null=True)
    clss = models.CharField(max_length=200, null=True)
    inf_addr = models.CharField(max_length=200, null=True)
    var20 = models.CharField(max_length=200, null=True)
    propid = models.CharField(max_length=200, null=True)
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
    object_id = models.CharField(max_length=200, null=True)
    model_type = models.CharField(max_length=200, null=True)
    type_desc = models.CharField(max_length=200, null=True)
    frequency = models.CharField(max_length=200, null=True)
    majormed = models.CharField(max_length=200, null=True)
    youthhealth = models.CharField(max_length=200, null=True)
    socdis = models.CharField(max_length=200, null=True)
    socstrife = models.CharField(max_length=200, null=True)
    alcohol = models.CharField(max_length=200, null=True)
    violence = models.CharField(max_length=200, null=True)
    guns = models.CharField(max_length=200, null=True)
    used = models.CharField(max_length=200, null=True)

class AddressLatLog(models.Model):
    address = models.CharField(max_length=200, null=True)
    latitude = models.CharField(max_length=200, null=True)
    longitude = models.CharField(max_length=200, null=True)

class PropIdLatLong(models.Model):
    propid = models.CharField(primary_key=True, max_length=200)
    address = models.CharField(max_length=200, null=True)
    latitude = models.CharField(max_length=200, null=True)
    longitude = models.CharField(max_length=200, null=True)

class TigerData(models.Model):
    type = models.CharField(max_length=200, null=True)
    areaid = models.CharField(max_length=200, null=True)
    latitude = models.CharField(max_length=200, null=True)
    longitude = models.CharField(max_length=200, null=True)
    
#my_csv_list = CSVInspectionViolation.import_data(data = open("study_18864/Data/Database/InspectionViolations.csv"))

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
    propid = fields.CharField()
    parcel_num = fields.CharField()
    neighborhood = fields.CharField()
    location_zip =fields.CharField()
    channel_type = fields.CharField()
    reporter_city = fields.CharField()
    reporter_zip = fields.CharField()
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
    sam_id = fields.CharField()
    prop_type = fields.CharField()
    disp_grp = fields.CharField()
    type = fields.CharField()
    priority = fields.CharField()
    close_dt = fields.CharField()
    entry_dt = fields.CharField()
    disp_dt = fields.CharField()
    enrte_dt = fields.CharField()
    onscene_dt = fields.CharField()
    recieve_dt = fields.CharField()
    all_wait_tm = fields.CharField()
    all_entre_tm = fields.CharField()
    all_onscene_tm = fields.CharField()
    all_dsip_tm = fields.CharField()
    comp_src = fields.CharField()
    clss = fields.CharField()
    inf_addr = fields.CharField()
    var20 = fields.CharField()
    propid = fields.CharField()
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
    object_id = fields.CharField()
    model_type = fields.CharField()
    type_desc = fields.CharField()
    frequency = fields.CharField()
    majormed = fields.CharField()
    youthhealth = fields.CharField()
    socdis = fields.CharField()
    socstrife = fields.CharField()
    alcohol = fields.CharField()
    violence = fields.CharField()
    guns = fields.CharField()
    used = fields.CharField()

    class Meta:
        delimiter = ","
        dbModel = Calls

class BostonCRM(models.Model):
    case_enquiry_id = models.IntegerField(null=True) #int
    case_reference = models.CharField(max_length=200, null=True)
    open_dt = models.DateField(null=True) #date
    close_dt = models.DateField(null=True) #date
    subject = models.CharField(max_length=200, null=True)
    reason = models.CharField(max_length=200, null=True)
    type = models.CharField(max_length=200, null=True)
    case_x = models.FloatField(null=True) #float
    case_y = models.FloatField(null=True) #float
    location = models.CharField(max_length=200, null=True)
    propid = models.CharField(max_length=200, null=True)
    parcel_num = models.CharField(max_length=200, null=True)
    neighborhood = models.CharField(max_length=200, null=True)
    location_zip = models.CharField(max_length=200, null=True)
    channel_type = models.CharField(max_length=200, null=True)
    reporter_city = models.CharField(max_length=200, null=True)
    reporter_zip = models.CharField(max_length=200, null=True)
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
    sam_id = models.IntegerField(null=True)
    prop_type = models.CharField(max_length=200, null=True)
    disp_grp = models.CharField(max_length=200, null=True)
    type = models.CharField(max_length=200, null=True)
    priority = models.IntegerField(null=True)
    close_dt = models.DateField(null=True)
    entry_dt = models.DateField(null=True)
    disp_dt = models.DateField(null=True)
    enrte_dt = models.DateField(null=True)
    onscene_dt = models.DateField(null=True)
    recieve_dt = models.DateField(null=True)
    all_wait_tm = models.IntegerField(null=True)
    all_entre_tm = models.IntegerField(null=True)
    all_onscene_tm = models.IntegerField(null=True)
    all_dsip_tm = models.IntegerField(null=True)
    comp_src = models.CharField(max_length=200,null=True)
    clss = models.CharField(max_length=200, null=True)
    inf_addr = models.CharField(max_length=200, null=True)
    var20 = models.CharField(max_length=200, null=True)
    propid = models.CharField(max_length=200, null=True)
    locationid = models.FloatField(null=True)
    ref_id = models.FloatField(null=True)
    x = models.FloatField(null=True)
    y = models.FloatField(null=True)
    landuse = models.CharField(max_length=200, null=True)
    blk_id = models.IntegerField(null=True)
    bg_id = models.IntegerField(null=True)
    ct_id = models.IntegerField(null=True)
    nbhd = models.CharField(max_length=200, null=True) 
    nsa_name = models.CharField(max_length=200, null=True)
    object_id = models.CharField(max_length=200, null=True)
    model_type = models.CharField(max_length=200, null=True)
    type_desc = models.CharField(max_length=200, null=True) 
    frequency = models.IntegerField(null=True)
    majormed = models.BooleanField(default=False)
    youthhealth = models.BooleanField(default=False)
    socdis = models.BooleanField(default=False)
    socstrife = models.BooleanField(default=False)
    alcohol = models.BooleanField(default=False)
    violence = models.BooleanField(default=False)
    guns = models.BooleanField(default=False)
    used = models.BooleanField(default=False)


