#!~/Code/broken_windows/manage.py
from boston_disorder.models import *
from django.db.models import *
from collections import defaultdict
from datetime import date
import time
import os
import sys
import time
import datetime

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "broken_windows.settings")
    
    #crime_data = Crime.objects.all()
    #min_date = Crime.objects.all().aggregate(Min('fromdate'))
    #max_date = Crime.objects.all().aggregate(Max('fromdate'))
    #print "Min date %s , Max date %s"%(min_date,max_date)
    
    #crime_neighborhoods = Crime.objects.values('neighborhood').annotate(Count('pk')).order_by('pk__count')
    
    #specific_neighborhood_crime = Crime.objects.filter(neighborhood='MID DORCHESTER').values('crimecode_description').annotate(Count('pk')).order_by('pk__count')
    
    #weapons = Crime.objects.values('weapon_type').annotate(Count('pk')).order_by('pk__count')

    #service_request_neighborhoods = ServiceRequest.objects.filter(case_status="Closed").values('neighborhood').annotate(Count('pk')).order_by('pk__count')
    """service_request_neighborhoods = ServiceRequest.objects.filter(case_status="Closed").values('neighborhood', 'open_dt', 'closed_dt')
    
    neighborhood_dict = defaultdict(list)
    for item in service_request_neighborhoods:
        neighborhood = item['neighborhood']
        open_dt = time.strptime(item['open_dt'], "%Y-%m-%dT%H:%M:%S")#"%m/%d/%Y %I:%M:%S %p")
        close_dt = time.strptime(item['closed_dt'], "%Y-%m-%dT%H:%M:%S")#"%m/%d/%Y %I:%M:%S %p")
        open_date = date(open_dt.tm_year, open_dt.tm_mon, open_dt.tm_mday)
        close_date = date(close_dt.tm_year, close_dt.tm_mon, close_dt.tm_mday)
        delta = close_date - open_date
        #print delta.days
        neighborhood_dict[neighborhood].append(delta.days)

    print "COMPUTING NEIGHBORHOODS"
    for neighborhood, delta_list in neighborhood_dict.items():
        print "In %s - avg response time for %s service requests was %s days"%(neighborhood, len(delta_list), sum(delta_list)/len(delta_list))
    #b_and_e = Crime.objects.filter(crimecode_description__contains="B&E").values('neighborhood').annotate(n=Count('pk'))

    """

    """permits = HansonPermits.objects.values('permittype').annotate(Count('pk')).order_by('-pk__count')
    for permit in permits:
        print permit"""

    """calls = CAD.objects.values('violent').annotate(Count('pk')).order_by('-pk__count')
    for call in calls:
        print call
    """
    """
    ivs = InspectionViolation.objects.all()
    errors = []
    for i, iv in enumerate(ivs):
        try:
            struct = time.strptime(iv.violationdate, "%m/%d/%Y")
            date = datetime.date(*struct[:3])
        except Exception as e:
            print e
            date = None
        try:
            new_iv = BostonInspectionViolation(
                casenumber = unicode(iv.casenumber) if iv.casenumber not in ['NULL', ''] else None,
                ticketnumber = unicode(iv.ticketnumber) if iv.ticketnumber not in ['NULL', ''] else None,
                violationdate = date,
                result = unicode(iv.result) if iv.result not in ['NULL', ''] else None,
                caseinfostatus = unicode(iv.caseinfostatus) if iv.caseinfostatus not in ['NULL', ''] else None,
                amt = int(iv.amt) if iv.amt not in ['NULL', ''] else None,
                stat = unicode(iv.stat) if iv.stat not in ['NULL', ''] else None,
                namefirst = unicode(iv.namefirst) if iv.namefirst not in ['NULL', ''] else None,
                namelast = unicode(iv.namelast) if iv.namelast not in ['NULL', ''] else None,
                addressid = int(iv.addressid) if iv.addressid not in ['NULL', ''] else None,
                ward = int(iv.ward) if iv.ward not in ['NULL', ''] else None,
                city = unicode(iv.city) if iv.city not in ['NULL', ''] else None,
                suffix = unicode(iv.suffix) if iv.suffix not in ['NULL', ''] else None,
                state = unicode(iv.state) if iv.state not in ['NULL', ''] else None,
                stname = unicode(iv.stname) if iv.stname not in ['NULL', ''] else None,
                stno = int(iv.stno) if iv.stno not in ['NULL', ''] else None,
                stnohi = int(iv.stnohi) if iv.stnohi not in ['NULL', ''] else None,
                zip = int(iv.zip) if iv.zip not in ['NULL', ''] else None,
                gpsy = float(iv.gpsy) if iv.gpsy not in ['NULL', ''] else None,
                gpsx = float(iv.gpsx) if iv.gpsx not in ['NULL', ''] else None,
                addrkey = unicode(iv.addrkey) if iv.addrkey not in ['NULL', ''] else None,
                feelastmoddte = int(iv.feelastmoddte) if iv.feelastmoddte not in ['NULL', ''] else None,
                pri = unicode(iv.pri) if iv.pri not in ['NULL', ''] else None,
                failedcode = int(iv.descript) if iv.failedcode not in ['NULL', ''] else None,
                descript = unicode(iv.paiddttm) if iv.descript not in ['NULL', ''] else None,
                paiddttm = unicode(iv.waived) if iv.paiddttm not in ['NULL', ''] else None,
                waived = unicode(iv.liened) if iv.waived not in ['NULL', ''] else None,
                liened = unicode(iv.comments) if iv.liened not in ['NULL', ''] else None,
                comments = None)
            if not i % 500:
                print i
            new_iv.save()
        except Exception as e:
            errors.append((i, e))
            print e
            continue
            """
    """
    calls = CAD.objects.filter(priority='.')
    errors = []
    for i, call in enumerate(calls):
        try:
            struct = time.strptime(call.close_dt, "%d-%b-%y")
            date = datetime.date(*struct[:3])
        except Exception as e:
            print e
            date = None
        try:
            new_call = BostonCAD(
                inc_no = unicode(call.inc_no) if call.inc_no not in ['NULL', ''] else None,
                inf_addr = unicode(call.inf_addr) if call.inf_addr not in ['NULL', ''] else None,
                address_text = unicode(call.address_text) if call.address_text not in ['NULL', ''] else None,
                matched = unicode(call.matched) if call.matched not in ['NULL', ''] else None,
                match_score = int(call.match_score) if call.match_score not in ['NULL', ''] else None,
                match_test = unicode(call.match_test) if call.match_test not in ['NULL', ''] else None,
                match_type = unicode(call.match_type) if call.match_type not in ['NULL', ''] else None,
                match_id = int(call.match_id) if call.match_id not in ['NULL', ''] else None,
                matchxcoordinate = float(call.matchxcoordinate) if call.matchxcoordinate not in ['NULL', ''] else None,
                matchycoordinate = float(call.matchycoordinate) if call.matchycoordinate not in ['NULL', ''] else None,
                match_codes = unicode(call.match_codes) if call.match_codes not in ['NULL', ''] else None,
                propid = unicode(call.propid) if call.propid not in ['NULL', ''] else None,
                final_type = unicode(call.final_type) if call.final_type not in ['NULL', ''] else None,
                priority = int(call.priority) if call.priority not in ['NULL', '', '.'] else None,
                close_dt = date,
                type_desc = unicode(call.type_desc) if call.type_desc not in ['NULL', ''] else None,
                disorder = bool(int(call.disorder)) if call.disorder not in ['NULL', ''] else None,
                medemerg = bool(int(call.medemerg)) if call.medemerg not in ['NULL', ''] else None,
                violent = bool(int(call.violent)) if call.violent not in ['NULL', ''] else None)
            new_call.save()
            if not i % 500:
                print i
        except Exception as e:
            print e
            errors.append((i, e))
            continue
    print errors
    """
    """
    fires = Fire.objects.all()
    errors = []
    for i, fire in enumerate(fires[1:]):
        try:
            struct = time.strptime(fire.aim_date, "%m/%d/%Y")
            date = datetime.date(*struct[:3])
        except Exception as e:
            print e
            date = None
        try:
            new_fire = BostonFire(
                status = unicode(fire.status) if fire.status not in ['NULL', ''] else None,
                score = float(fire.score) if fire.score not in ['NULL', ''] else None,
                match_type = unicode(fire.match_type) if fire.match_type not in ['NULL', ''] else None,
                match_addr = unicode(fire.match_addr) if fire.match_addr not in ['NULL', ''] else None,
                side = unicode(fire.side) if fire.side not in ['NULL', ''] else None,
                ref_id = int(fire.ref_id) if fire.ref_id not in ['NULL', ''] else None,
                x = float(fire.x) if fire.x not in ['NULL', ''] else None,
                y = float(fire.y) if fire.y not in ['NULL', ''] else None,
                user_fld = int(fire.user_fld) if fire.user_fld not in ['NULL', ''] else None,
                addr_type = unicode(fire.addr_type) if fire.addr_type not in ['NULL', ''] else None,
                arc_street = unicode(fire.arc_street) if fire.arc_street not in ['NULL', ''] else None,
                arc_zip = int(fire.arc_zip) if fire.arc_zip not in ['NULL', ''] else None,
                inci_no = unicode(fire.inci_no) if fire.inci_no not in ['NULL', ''] else None,
                aim_date = date,
                aim_time = None,
                inci_type = int(fire.inci_type) if fire.inci_type not in ['NULL', ''] else None,
                descript = unicode(fire.descript) if fire.descript not in ['NULL', ''] else None,
                prop_loss = int(fire.prop_loss) if fire.prop_loss not in ['NULL', ''] else None,
                cont_loss = int(fire.cont_loss) if fire.cont_loss not in ['NULL', ''] else None,
                aim_type = int(fire.aim_type) if fire.aim_type not in ['NULL', ''] else None,
                district = int(fire.district) if fire.district not in ['NULL', ''] else None,
                cause_ign = int(fire.cause_ign) if fire.cause_ign not in ['NULL', ''] else None,
                descript_b = unicode(fire.descript_b) if fire.descript_b not in ['NULL', ''] else None,
                addr_typ_1 = unicode(fire.addr_typ_1) if fire.addr_typ_1 not in ['NULL', ''] else None,
                number = int(fire.number) if fire.number not in ['NULL', ''] else None,
                st_prefix = unicode(fire.st_prefix) if fire.st_prefix not in ['NULL', ''] else None,
                street = unicode(fire.street) if fire.street not in ['NULL', ''] else None,
                st_type = unicode(fire.st_type) if fire.st_type not in ['NULL', ''] else None,
                addr_2 = unicode(fire.addr_2) if fire.addr_2 not in ['NULL', ''] else None,
                apt_room = unicode(fire.apt_room) if fire.apt_room not in ['NULL', ''] else None,
                city = unicode(fire.city) if fire.city not in ['NULL', ''] else None,
                state = unicode(fire.state) if fire.state not in ['NULL', ''] else None,
                zip = int(fire.zip) if fire.zip not in ['NULL', ''] else None,
                how_receiv = unicode(fire.how_receiv) if fire.how_receiv not in ['NULL', ''] else None,
                total_loss = int(fire.total_loss) if fire.total_loss not in ['NULL', ''] else None,
                address = unicode(fire.address) if fire.address not in ['NULL', ''] else None,
                address_zip = unicode(fire.address_zip) if fire.address_zip not in ['NULL', ''] else None,
                locationid = int(fire.locationid) if fire.locationid not in ['NULL', ''] else None)
            new_fire.save()
            if not i % 500:
                print i
        except Exception as e:
            print e
            errors.append((i, e))
            continue
    print errors
    """
    """
    permits = HansonPermits.objects.all()
    errors = []
    for i, permit in enumerate(permits[1:]):
        try:
            new_permit = BostonPermits(
                apbldkey = int(permit.apbldkey) if permit.apbldkey not in ['NULL', '', ' '] else None,
                permittype = unicode(permit.permittype) if permit.permittype not in ['NULL', '', ' '] else None,
                adddttm = unicode(permit.adddttm) if permit.adddttm not in ['NULL', '', ' '] else None,
                moddttm = unicode(permit.moddttm) if permit.moddttm not in ['NULL', '', ' '] else None,
                expdttm = unicode(permit.expdttm) if permit.expdttm not in ['NULL', '', ' '] else None,
                permitstatus = unicode(permit.permitstatus) if permit.permitstatus not in ['NULL', '', ' '] else None,
                worktype = unicode(permit.worktype) if permit.worktype not in ['NULL', '', ' '] else None,
                permitnumber = unicode(permit.permitnumber) if permit.permitnumber not in ['NULL', '', ' '] else None,
                addrkey = int(permit.addrkey) if permit.addrkey not in ['NULL', '', ' '] else None,
                block = unicode(permit.block) if permit.block not in ['NULL', '', ' '] else None,
                ward = int(permit.ward) if permit.ward not in ['NULL', '', ' '] else None,
                predir = unicode(permit.predir) if permit.predir not in ['NULL', '', ' '] else None,
                stno = unicode(permit.stno) if permit.stno not in ['NULL', '', ' '] else None,
                stnohi = unicode(permit.stnohi) if permit.stnohi not in ['NULL', '', ' '] else None,
                stname = unicode(permit.stname) if permit.stname not in ['NULL', '', ' '] else None,
                suffix = unicode(permit.suffix) if permit.suffix not in ['NULL', '', ' '] else None,
                city = unicode(permit.city) if permit.city not in ['NULL', '', ' '] else None,
                zip = int(permit.zip) if permit.zip not in ['NULL', '', ' '] else None,
                gpsy = float(permit.gpsy) if permit.gpsy not in ['NULL', '', ' '] else None,
                gpsx = float(permit.gpsx) if permit.gpsx not in ['NULL', '', ' '] else None,
                issdttm = unicode(permit.issdttm) if permit.issdttm not in ['NULL', '', ' '] else None,
                pri = unicode(permit.pri) if permit.pri not in ['NULL', '', ' '] else None,
                occupancytype = unicode(permit.occupancytype) if permit.occupancytype not in ['NULL', '', ' '] else None,
                coodttm = unicode(permit.coodttm) if permit.coodttm not in ['NULL', '', ' '] else None,
                tmpcoodttm = unicode(permit.tmpcoodttm) if permit.tmpcoodttm not in ['NULL', '', ' '] else None,
                permittypedescr = unicode(permit.permittypedescr) if permit.permittypedescr not in ['NULL', '', ' '] else None,
                bldgarea = float(permit.bldgarea) if permit.bldgarea not in ['NULL', '', ' '] else None,
                finaldttm = unicode(permit.finaldttm) if permit.finaldttm not in ['NULL', '', ' '] else None,
                descript = unicode(permit.descript) if permit.descript not in ['NULL', '', ' '] else None)
            new_permit.save()
            if not i % 250:
                print i
        except Exception as e:
            print i, e
            errors.append((i, e))

    #print errors
    """
    #print "HERE"
    #my_csv_list = CSVCRM.import_data(data = open("study_18864/Data/Database/CRMMaster.csv"))
    """
    HOUSING_ISSUES_CODES = [
        "Bed Bugs", #12, #Bed Bugs
        "Breathe Easy",#18, #Breathe Easy
        "Chrnoic Dampness / Mold",#26, #Chrnoic Dampness / Mold
        "Heat - Excessive, Insufficient",#50, #Heat - Excessive, Insufficient
        "Maintenance Complaint - Residential",#68, #Maintenance Complaint - Residential
        "Mice Infestation - Residential",#71, #Mice Infestation - Residential
        "Pest Infestation - Residential",#107, #Pest Infestation - Residential
        "Poor Ventilation",#113, #Poor Ventilation
        "Squalid Living Conditions",#147, #Squalid Living Conditions
        "Unsatisfactory Living Conditions",#165, #Unsatisfactory Living Conditions
        "Unsatisfactory Utilities - Electrical, Plumbing",#166, #Unsatisfactory Utilities - Electrical, Plumbing
    ]

    UNCIVIL_USE_OF_SPACE_CODES = [
        "Abandoned Building",#3, #Abandoned Building
        "Illegal Occupancy",#55, #Illegal Occupancy
        "Illegal Rooming House",#57, #Illegal Rooming House
        "Maintenance - Homeowner",#67, #Maintenance - Homeowner
        "Parking on Front/Back Yards (Illegal Parking)",#103, #Parking on Front/Back Yards (Illegal Parking)
        "Poor Conditions of Property",#112, #Poor Conditions of Property
        "Trash on Vacant Lot",#157, #Trash on Vacant Lot
    ]

    BIG_BUILDINGS_CODES = [
        "Big Buildings Enforcement",#13, #Big Buildings Enforcement
        "Big Buildings Online Request",#14, #Big Buildings Online Request
        "Big Buildings Resident Complaint",#15, #Big Buildings Resident Complaint
    ]

    GRAFFITI_CODES = [
        "Graffiti Removal",#49, #Graffiti Removal
        "PWD Graffiti",#96, #PWD Graffiti
    ]

    TRASH_CODES = [
        "Abandoned Bicycle",#2, #Abandoned Bicycle
        "Empty Litter Basket",#37, #Empty Litter Basket
        "Illegal Dumping",#54, #Illegal Dumping
        "Improper Storage of Trash (Barrels)",#60, #Improper Storage of Trash (Barrels)
        "Rodent Activity",#131, #Rodent Activity
    ]
    filters = HOUSING_ISSUES_CODES + UNCIVIL_USE_OF_SPACE_CODES + BIG_BUILDINGS_CODES + GRAFFITI_CODES + TRASH_CODES
    print "imported"
    crm = CRM.objects.filter(type__in=filters)
    errors = []
    for i, entry in enumerate(crm[2:]):
        odate = None
        cdate = None
        if entry.open_dt not in ['NULL', '', ' ']:
            try:
                ostruct = time.strptime(entry.open_dt, "%m/%d/%Y")
                odate = datetime.date(*ostruct[:3])
            except Exception as e:
                print e
        if entry.close_dt not in ['NULL', '', ' ']:
            try:
                cstruct = time.strptime(entry.close_dt, "%m/%d/%Y")
                cdate = datetime.date(*cstruct[:3])
            except Exception as e:
                print e
        try:
            new_entry = BostonCRM(
                case_enquiry_id = int(entry.case_enquiry_id) if entry.case_enquiry_id not in ['NULL', '', ' '] else None,
                case_reference = int(entry.case_reference) if entry.case_reference not in ['NULL', '', ' '] else None,
                open_dt = odate,
                close_dt = cdate,
                subject = unicode(entry.subject) if entry.subject not in ['NULL', '', ' '] else None,
                reason = unicode(entry.reason) if entry.reason not in ['NULL', '', ' '] else None,
                type = unicode(entry.type) if entry.type not in ['NULL', '', ' '] else None,
                case_x = float(entry.case_x) if entry.case_x not in ['NULL', '', ' '] else None,
                case_y = float(entry.case_y) if entry.case_y not in ['NULL', '', ' '] else None,
                location = unicode(entry.location) if entry.location not in ['NULL', '', ' '] else None,
                city = unicode(entry.city) if entry.city not in ['NULL', '', ' '] else None,
                state = unicode(entry.state) if entry.state not in ['NULL', '', ' '] else None,
                propid = unicode(entry.propid) if entry.propid not in ['NULL', '', ' '] else None,
                parcel_num = unicode(entry.parcel_num) if entry.parcel_num not in ['NULL', '', ' '] else None,
                neighborhood = unicode(entry.neighborhood) if entry.neighborhood not in ['NULL', '', ' '] else None,
                channel_type = unicode(entry.channel_type) if entry.channel_type not in ['NULL', '', ' '] else None,
                party_id = int(entry.party_id) if entry.party_id not in ['NULL', '', ' '] else None,
                source = unicode(entry.source) if entry.source not in ['NULL', '', ' '] else None,
                locationid = int(entry.locationid) if entry.locationid not in ['NULL', '', ' '] else None,
                ref_id = int(entry.ref_id) if entry.ref_id not in ['NULL', '', ' '] else None,
                x = float(entry.x) if entry.x not in ['NULL', '', ' '] else None,
                y = float(entry.y) if entry.y not in ['NULL', '', ' '] else None,
                landuse = unicode(entry.landuse) if entry.landuse not in ['NULL', '', ' '] else None,
                blk_id = int(entry.blk_id) if entry.blk_id not in ['NULL', '', ' '] else None,
                bg_id = int(entry.bg_id) if entry.bg_id not in ['NULL', '', ' '] else None,
                ct_id = int(entry.ct_id) if entry.ct_id not in ['NULL', '', ' '] else None,
                nbhd = unicode(entry.nbhd) if entry.nbhd not in ['NULL', '', ' '] else None,
                nsa_name = unicode(entry.nsa_name) if entry.nsa_name not in ['NULL', '', ' '] else None,
                objectid = int(entry.objectid) if entry.objectid not in ['NULL', '', ' '] else None,
                #code = int(entry.code) if entry.code not in ['NULL', '', ' '] else None,
                public = bool(int(entry.public)) if entry.public not in ['NULL', '', ' '] else None,
                unciviluse = bool(int(entry.unciviluse)) if entry.unciviluse not in ['NULL', '', ' '] else None,
                housing = bool(int(entry.housing)) if entry.housing not in ['NULL', '', ' '] else None,
                bigbuild = bool(int(entry.bigbuild)) if entry.bigbuild not in ['NULL', '', ' '] else None,
                graffiti = bool(int(entry.graffiti)) if entry.graffiti not in ['NULL', '', ' '] else None,
                trash = bool(int(entry.trash)) if entry.trash not in ['NULL', '', ' '] else None,
                privateneglect = bool(int(entry.privateneglect)) if entry.privateneglect not in ['NULL', '', ' '] else None,
                problem = bool(int(entry.problem)) if entry.problem not in ['NULL', '', ' '] else None,
                publicdenig = bool(int(entry.publicdenig)) if entry.publicdenig not in ['NULL', '', ' '] else None,
                my = int(entry.my) if entry.my not in ['NULL', '', ' '] else None,
                bg = bool(int(entry.bg)) if entry.bg not in ['NULL', '', ' '] else None)
            new_entry.save()
            if not i % 500:
                print i
        except Exception as e:
            print i, e
            errors.append((i, e))
    print errors

    bgs = BlockGroup.objects.all()
    errors = []
    for i, bg in enumerate(bgs[1:]):
        try:
            new_entry = BostonBlockGroup(
                objectid = int(bg.objectid) if bg.objectid not in ['NULL', '', ' '] else None,
                area = float(bg.area) if bg.area not in ['NULL', '', ' '] else None,
                perimeter = float(bg.perimeter) if bg.perimeter not in ['NULL', '', ' '] else None,
                state = int(bg.state) if bg.state not in ['NULL', '', ' '] else None,
                county = int(bg.county) if bg.county not in ['NULL', '', ' '] else None,
                tract = int(bg.tract) if bg.tract not in ['NULL', '', ' '] else None,
                blockgroup = int(bg.blockgroup) if bg.blockgroup not in ['NULL', '', ' '] else None,
                bg_id = int(bg.bg_id) if bg.bg_id not in ['NULL', '', ' '] else None,
                ct_id = int(bg.ct_id) if bg.ct_id not in ['NULL', '', ' '] else None,
                blk_count = int(bg.blk_count) if bg.blk_count not in ['NULL', '', ' '] else None,
                logrecno = int(bg.logrecno) if bg.logrecno not in ['NULL', '', ' '] else None,
                dry_acres = float(bg.dry_acres) if bg.dry_acres not in ['NULL', '', ' '] else None,
                dry_sqmi = float(bg.dry_sqmi) if bg.dry_sqmi not in ['NULL', '', ' '] else None,
                dry_sqkm = float(bg.dry_sqkm) if bg.dry_sqkm not in ['NULL', '', ' '] else None,
                shape_area = float(bg.shape_area) if bg.shape_area not in ['NULL', '', ' '] else None,
                shape_len = float(bg.shape_len) if bg.shape_len not in ['NULL', '', ' '] else None,
                hoods_pd = float(bg.hoods_pd) if bg.hoods_pd not in ['NULL', '', ' '] else None,
                nbhd = unicode(bg.nbhd) if bg.nbhd not in ['NULL', '', ' '] else None, 
                nbhdCRM = unicode(bg.nbhdCRM) if bg.nbhdCRM not in ['NULL', '', ' '] else None,
                nsa_id = unicode(bg.nsa_id) if bg.nsa_id not in ['NULL', '', ' '] else None,
                nsa_name = unicode(bg.nsa_name) if bg.nsa_name not in ['NULL', '', ' '] else None,
                bg_id_1 = float(bg.bg_id_1) if bg.bg_id_1 not in ['NULL', '', ' '] else None,
                homeowners = float(bg.homeowners) if bg.homeowners not in ['NULL', '', ' '] else None,
                medincome = float(bg.medincome) if bg.medincome not in ['NULL', '', ' '] else None,
                propwhite = float(bg.propwhite) if bg.propwhite not in ['NULL', '', ' '] else None,
                propblack = float(bg.propblack) if bg.propblack not in ['NULL', '', ' '] else None,
                propasian = float(bg.propasian) if bg.propasian not in ['NULL', '', ' '] else None,
                prophisp = float(bg.prophisp) if bg.prophisp not in ['NULL', '', ' '] else None,
                medage = float(bg.medage) if bg.medage not in ['NULL', '', ' '] else None,
                propcollege = float(bg.propcollege) if bg.propcollege not in ['NULL', '', ' '] else None,
                totalpop = float(bg.totalpop) if bg.totalpop not in ['NULL', '', ' '] else None,
                popden = float(bg.popden) if bg.popden not in ['NULL', '', ' '] else None)
            new_entry.save()
        except Exception as e:
            print e
t = CSVCalls.import_data(data = open("/Users/jeffreyguion/Documents/Code/city_of_boston/other_data/CADCalls.csv"))

    calls = Calls.objects.all()
    errors = []
    for i, call in enumerate(calls[1:]):
        if call.close_dt not in ['NULL', '', ' ']:
            try:
                cstruct = time.strptime(call.close_dt, "%m/%d/%Y")
                cdate = datetime.date(*cstruct[:3])
            except Exception as e:
                print e
        try:
            new_entry = Boston911Calls(
                inc_no = unicode(call.inc_no) if call.inc_no not in ['NULL', '', ' '] else None,
                inf_addr = unicode(call.inf_addr) if call.inf_addr not in ['NULL', '', ' '] else None,
                match_text = unicode(call.match_text) if call.match_text not in ['NULL', '', ' '] else None,
                propid = unicode(call.propid) if call.propid not in ['NULL', '', ' '] else None,
                type = unicode(call.type) if call.type not in ['NULL', '', ' '] else None,
                model_type = unicode(call.model_type) if call.model_type not in ['NULL', '', ' '] else None,
                priority = int(call.priority) if call.priority not in ['NULL', '', ' '] else None,
                close_dt = cdate,
                type_desc = unicode(call.type_desc) if call.type_desc not in ['NULL', '', ' '] else None,
                locationid = int(call.locationid) if call.locationid not in ['NULL', '', ' '] else None,
                objectid = unicode(call.objectid) if call.objectid not in ['NULL', '', ' '] else None,
                ref_id = int(call.ref_id) if call.ref_id not in ['NULL', '', ' '] else None,
                x = float(call.x) if call.x not in ['NULL', '', ' '] else None,
                y = float(call.y) if call.y not in ['NULL', '', ' '] else None,
                blk_id = int(call.blk_id) if call.blk_id not in ['NULL', '', ' '] else None,
                bg_id = int(call.bg_id) if call.bg_id not in ['NULL', '', ' '] else None,
                ct_id = int(call.ct_id) if call.ct_id not in ['NULL', '', ' '] else None,
                nsa_name = unicode(call.nsa_name) if call.nsa_name not in ['NULL', '', ' '] else None,
                nbhd = unicode(call.nbhd) if call.nbhd not in ['NULL', '', ' '] else None, 
                socdis = bool(int(call.socdis)) if call.socdis not in ['NULL', '', ' '] else None,
                socstrife = bool(int(call.socstrife)) if call.socstrife not in ['NULL', '', ' '] else None,
                alcohol = bool(int(call.alcohol)) if call.alcohol not in ['NULL', '', ' '] else None,
                violence = bool(int(call.violence)) if call.violence not in ['NULL', '', ' '] else None,
                guns = bool(int(call.guns)) if call.guns not in ['NULL', '', ' '] else None,
                no_med = bool(int(call.no_med)) if call.no_med not in ['NULL', '', ' '] else None,
                majormed = bool(int(call.majormed)) if call.majormed not in ['NULL', '', ' '] else None,
                youthhealth = bool(int(call.youthhealth)) if call.youthhealth not in ['NULL', '', ' '] else None
                )
            new_entry.save()
            if not i % 100:
                print i
        except Exception as e:
            print e


i = 17159
tiger = TigerData.objects.all()
while i >= 10231:
    td = tiger[i]
    try:
        tiger.get(areaid=td.areaid)
    except Exception as e:
        print e
        td.delete()
    i -= 1
"""

    all_addresses = AddressLatLog.objects.values_list("address", "latitude", "longitude")
    all_dict1 = dict((x[0], x) for x in all_addresses)
    all_dict2 = {}
    a_dict = defaultdict(list)
    pll_dict = {}
    duplicate_count = 0
    different_lat_count = 0
    different_long_count = 0
    for a, lat, lng in all_addresses:
        info = a.lower().split(',')
        address = None
        city = None
        state = None
        zipcode = None
        if len(info) <= 1:
            info = a.lower().split('  ')

        address = info[0].strip()
        a_dict[address].append((a,lat,lng))
        if len(info) > 1:
            city = info[1].strip()
            if all_dict2.get((address, city)):
                latitude, longitude = all_dict2.get((address, city))
                duplicate_count += 1
                if latitude != lat:
                    #print "%s -- %s ... Old Lat %s , New Lat %s"%(address, city, latitude, lat)
                    different_lat_count += 1
                if longitude != lng:
                    #print "%s -- %s ... Old long %s , New long %s"%(address, city, longitude, lng)
                    different_long_count += 1
            else:
                all_dict2[(address,city)] = (lat,lng)

            if len(info) > 2:
                state = info[2].strip()
                if len(info) > 3:
                    zipcode = info[3].strip()

    #for a, info in a_dict.items():
    #    if len(info) > 1:
    #        print info


    miss_count = 0
    bad_count = 0
    crm = BostonCRM.objects.values_list('location', 'propid')
    for location, propid in crm:
        if not location or not propid:
            bad_count += 1
            continue
        info = location.lower().split('  ')
        address = info[0].strip()
        if len(info) > 1:
            city = info[1].strip()

            lat, lng = all_dict2.get((address, city), (None,None))
            if lat is None or lng is None:
                attempt = a_dict[address]
                if attempt:
                    lat = attempt[0][1]
                    lng = attempt[0][2]
                    pll_dict[propid] = (location,lat,lng)
                else:
                    miss_count += 1
            else:
                pll_dict[propid] = (location,lat,lng)
        else:
            bad_count += 1

    cad = Boston911Calls.objects.values_list('inf_addr', 'propid')
    bad_cad = 0
    cad_miss = 0
    for location, propid in cad:
        if not location or not propid:
            bad_cad += 1
            continue
        info = location.lower().split('  ')
        address = info[0].strip()

        attempt = a_dict[address]
        if attempt:
            lat = attempt[0][1]
            lng = attempt[0][2]
            pll_dict[propid] = (location, lat,lng)
        else:
            cad_miss += 1

    i =0
    for propid, info in pll_dict.items():
        p = PropIdLatLong(
            propid=propid,
            address=info[0],
            latitude=info[1],
            longitude=info[2])
        p.save()
        if i % 300:
            print i
        i += 1


    print "***Done****"
    print "DUPLICATES = %s"%duplicate_count
    print "diff lats = %s"%different_lat_count
    print "diff long = %s"%different_long_count

    print "crm misses %s"%miss_count
    print "crm bad locations %s"%bad_count

    print "cad misses %s"%cad_miss
    print "cad bad locations %s"%bad_cad
    print len(all_addresses)
    print len(all_dict2)
    print len(pll_dict)





