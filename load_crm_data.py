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

### RUN THIS FIRST IN PYTHON SHELL
#   t = CSVCRM.import_data(data = open("/Path/to/CRMMaster.csv"))
###

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

NO_FACTOR_CODES = [
    "Illegal Auto Body Shop",#53, #Illegal Auto Body Shop
    "Illegal Posting of Signs",#56, #Illegal Posting of Signs
    "Illegal Use",#58, #Illegal Use
    "Overflowing or Un-kept Dumpster",#95, #Overflowing or Un-kept Dumpster
    "Pigeon Infestation",#110, #Pigeon Infestation
]

filters = HOUSING_ISSUES_CODES + UNCIVIL_USE_OF_SPACE_CODES + BIG_BUILDINGS_CODES + GRAFFITI_CODES + TRASH_CODES


if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "broken_windows.settings")
    print "start"
    crm = CRM.objects.filter(type__in=filters)
    errors = []
    for i, entry in enumerate(crm[1:]):
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
                cstruct = time.strptime(entry.close_dt.split(".")[0], "%Y-%m-%d %H:%M:%S")
                cdate = datetime.date(*cstruct[:3])
            except Exception as e:
                print e
        try:
            new_entry = BostonCRM(
                case_enquiry_id = int(entry.case_enquiry_id) if entry.case_enquiry_id not in ['NULL', '', ' '] else None,
                case_reference = unicode(entry.case_reference) if entry.case_reference not in ['NULL', '', ' '] else None,
                open_dt = odate,
                close_dt = cdate,
                subject = unicode(entry.subject) if entry.subject not in ['NULL', '', ' '] else None,
                reason = unicode(entry.reason) if entry.reason not in ['NULL', '', ' '] else None,
                type = unicode(entry.type) if entry.type not in ['NULL', '', ' '] else None,
                case_x = float(entry.case_x) if entry.case_x not in ['NULL', '', ' '] else None,
                case_y = float(entry.case_y) if entry.case_y not in ['NULL', '', ' '] else None,
                location = unicode(entry.location) if entry.location not in ['NULL', '', ' '] else None,
                propid = unicode(entry.propid) if entry.propid not in ['NULL', '', ' '] else None,
                parcel_num = unicode(entry.parcel_num) if entry.parcel_num not in ['NULL', '', ' '] else None,
                neighborhood = unicode(entry.neighborhood) if entry.neighborhood not in ['NULL', '', ' '] else None,
                location_zip = unicode(entry.location_zip) if entry.location_zip not in ['NULL', '', ' '] else None,
                channel_type = unicode(entry.channel_type) if entry.channel_type not in ['NULL', '', ' '] else None,
                reporter_city = unicode(entry.reporter_city) if entry.reporter_city not in ['NULL', '', ' '] else None,
                reporter_zip = unicode(entry.reporter_zip) if entry.reporter_zip not in ['NULL', '', ' '] else None,
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
                publicdenig = bool(int(entry.publicdenig)) if entry.publicdenig not in ['NULL', '', ' '] else None)
            new_entry.save()

            if not i % 500:
                print i
        except Exception as e:
            print i, e
            errors.append((i, e))
    print errors

