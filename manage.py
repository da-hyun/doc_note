#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


# https://bernardparah.com/importing-data-from-a-csv-file-using-django-shell/

import csv
import pandas as pd
from doctor.models import Doctor

'''
with open('D:/ITWILL/project/data/doctor_py.csv','r') as f:
    dr = csv.DictReader(f)
    s = pd.DataFrame(dr)
ss = []
for i in range(len(s)):
    st = (s['PATIENT_ID'][i],s['CODE_NUMBER'][i],s['CODE_DESCRIPTION'][i],s['DATE'][i],s['AGE'][i],
          s['GENDER'][i],s['NOTES'][i],s['CURRENTRX'][i],s['CURRENTRX'][i],s['DOSE'][i],s['FREQUENCY'][i])
    ss.append(st)
for i in range(len(s)):
    Doctor.objects.create(PATIENT_ID=ss[i][0],CODE_NUMBER = ss[i][1],CODE_DESCRIPTION = ss[i][2],
                          DATE = ss[i][3],AGE = ss[i][4],GENDER = ss[i][5],NOTES = ss[i][6],
                          CURRENTRX = ss[i][7],DOSE = ss[i][8],FREQUENCY = ss[i][9])
'''
'''
# 0   PATIENT_ID        25521 non-null  int64         
# 1   CODE_NUMBER       25521 non-null  int64         
# 2   CODE_DESCRIPTION  25521 non-null  object        
# 3   DATE              25521 non-null  datetime64[ns]
# 4   AGE               25521 non-null  float64       
# 5   GENDER            25521 non-null  int64         
# 6   NOTES             25521 non-null  object        
# 7   CURRENTRX         25521 non-null  object        
# 8   DOSE              25521 non-null  object        
# 9   FREQUENCY         25521 non-null  object 
'''
