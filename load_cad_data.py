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
#   t = CSVCalls.import_data(data = open("/Path/to/CADCalls.csv"))
###
if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "broken_windows.settings")

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
            if not i % 200:
                print i
        except Exception as e:
            print e