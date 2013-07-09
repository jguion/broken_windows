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
from django.db.models import Q

PUBLIC_SOCIAL_DISORDER = {"socdis":"1"}
SOCIAL_STRIFE = {"socstrife":"1"}
ALCOHOL = {"alcohol":"1"}
INTERPERSONAL_VIOLENCE = {"violence":"1"}
GUNS = {"guns":"1"}
MAJOR_MEDICAL_EMERGENCIES = {"majormed":"1"}
RESPIRATORY_AND_OBGYN = {"youthhealth":"1"}
USED = {"used":"1"}

SOCIAL_DISORDER = Q(**PUBLIC_SOCIAL_DISORDER) | Q(**SOCIAL_STRIFE) | Q(**ALCOHOL)
VIOLENCE = Q(**INTERPERSONAL_VIOLENCE) | Q(**GUNS)
MEDICAL_EMERGENCIES = Q(**MAJOR_MEDICAL_EMERGENCIES) | Q(**RESPIRATORY_AND_OBGYN) | Q(**USED)
ALL_911_CALLS = Q(SOCIAL_DISORDER) | Q(VIOLENCE) | Q(MEDICAL_EMERGENCIES)

### RUN THIS FIRST IN PYTHON SHELL
#   t = CSVCalls.import_data(data = open("/Path/to/CADCalls.csv"))
###
if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "broken_windows.settings")
    calls = Calls.objects.filter(ALL_911_CALLS).all()
    errors = []
    print len(calls)
    for i, call in enumerate(calls[1:]):
        cdate = None
        edate = None
        ddate = None
        endate = None
        odate = None
        rdate = None
        if call.close_dt not in ['NULL', '', ' ']:
            try:
                cstruct = time.strptime(call.close_dt, "%d%b%y:%H:%M:%S")
                cdate = datetime.date(*cstruct[:3])
            except Exception as e:
                print e
        if call.entry_dt not in ['NULL', '', ' ']:
            try:
                estruct = time.strptime(call.entry_dt, "%d%b%y:%H:%M:%S")
                edate = datetime.date(*estruct[:3])
            except Exception as e:
                print e
        if call.disp_dt not in ['NULL', '', ' ']:
            try:
                dstruct = time.strptime(call.disp_dt, "%Y-%m-%d %H:%M:%S")
                ddate = datetime.date(*dstruct[:3])
            except Exception as e:
                print e
        if call.enrte_dt not in ['NULL', '', ' ']:
            try:
                enstruct = time.strptime(call.enrte_dt, "%Y-%m-%d %H:%M:%S")
                endate = datetime.date(*enstruct[:3])
            except Exception as e:
                print e
        if call.onscene_dt not in ['NULL', '', ' ']:
            try:
                ostruct = time.strptime(call.onscene_dt, "%Y-%m-%d %H:%M:%S")
                odate = datetime.date(*ostruct[:3])
            except Exception as e:
                print e
        if call.recieve_dt not in ['NULL', '', ' ']:
            try:
                rstruct = time.strptime(call.recieve_dt, "%Y-%m-%d %H:%M:%S")
                rdate = datetime.date(*rstruct[:3])
            except Exception as e:
                print e
        try:
            new_entry = Boston911Calls(
                inc_no = unicode(call.inc_no) if call.inc_no not in ['NULL', '', ' '] else None,
                sam_id = int(call.sam_id) if call.sam_id not in ['NULL', '', ' '] else None,
                prop_type = unicode(call.prop_type) if call.prop_type not in ['NULL', '', ' '] else None,
                disp_grp = unicode(call.disp_grp) if call.disp_grp not in ['NULL', '', ' '] else None,
                type = unicode(call.type) if call.type not in ['NULL', '', ' '] else None,
                priority = int(call.priority) if call.priority not in ['NULL', '', ' '] else None,
                close_dt = cdate,
                entry_dt = edate,
                disp_dt = ddate,
                enrte_dt = endate,
                onscene_dt = odate,
                recieve_dt = rdate,
                all_wait_tm = int(call.all_wait_tm) if call.all_wait_tm not in ['NULL', '', ' '] else None,
                all_entre_tm = int(call.all_entre_tm) if call.all_entre_tm not in ['NULL', '', ' '] else None,
                all_onscene_tm = int(call.all_onscene_tm) if call.all_onscene_tm not in ['NULL', '', ' '] else None,
                all_dsip_tm = int(call.all_dsip_tm) if call.all_dsip_tm not in ['NULL', '', ' '] else None,
                comp_src = unicode(call.comp_src) if call.comp_src not in ['NULL', '', ' '] else None,
                clss = unicode(call.clss) if call.clss not in ['NULL', '', ' '] else None,
                inf_addr = unicode(call.inf_addr) if call.inf_addr not in ['NULL', '', ' '] else None,
                var20 = unicode(call.var20) if call.var20 not in ['NULL', '', ' '] else None,
                propid = unicode(call.propid) if call.propid not in ['NULL', '', ' '] else None,
                locationid = float(call.locationid) if call.locationid not in ['NULL', '', ' '] else None,
                ref_id = float(call.ref_id) if call.ref_id not in ['NULL', '', ' '] else None,
                x = float(call.x) if call.x not in ['NULL', '', ' '] else None,
                y = float(call.y) if call.y not in ['NULL', '', ' '] else None,
                landuse = unicode(call.landuse) if call.landuse not in ['NULL', '', ' '] else None,
                blk_id = int(call.blk_id) if call.blk_id not in ['NULL', '', ' '] else None,
                bg_id = int(call.bg_id) if call.bg_id not in ['NULL', '', ' '] else None,
                ct_id = int(call.ct_id) if call.ct_id not in ['NULL', '', ' '] else None,
                nbhd = unicode(call.nbhd) if call.nbhd not in ['NULL', '', ' '] else None,
                nsa_name = unicode(call.nsa_name) if call.nsa_name not in ['NULL', '', ' '] else None,
                object_id = unicode(call.object_id) if call.object_id not in ['NULL', '', ' '] else None,
                model_type = unicode(call.model_type) if call.model_type not in ['NULL', '', ' '] else None,
                type_desc = unicode(call.type_desc) if call.type_desc not in ['NULL', '', ' '] else None,
                frequency = int(call.frequency) if call.frequency not in ['NULL', '', ' '] else None,
                majormed = bool(int(call.majormed)) if call.majormed not in ['NULL', '', ' '] else None,
                youthhealth = bool(int(call.youthhealth)) if call.youthhealth not in ['NULL', '', ' '] else None,
                socdis = bool(int(call.socdis)) if call.socdis not in ['NULL', '', ' '] else None,
                socstrife = bool(int(call.socstrife)) if call.socstrife not in ['NULL', '', ' '] else None,
                alcohol = bool(int(call.alcohol)) if call.alcohol not in ['NULL', '', ' '] else None,
                violence = bool(int(call.violence)) if call.violence not in ['NULL', '', ' '] else None,
                guns = bool(int(call.guns)) if call.guns not in ['NULL', '', ' '] else None,
                used = bool(int(call.used)) if call.used not in ['NULL', '', ' '] else None
                
                )
            new_entry.save()
            if not i % 200:
                print i
        except Exception as e:
            print "%s , %s"%(e,i)