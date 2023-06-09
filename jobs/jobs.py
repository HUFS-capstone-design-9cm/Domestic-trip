from django.conf import settings
from time import time
from datetime import datetime
from main.models import Traveler

timeZone = datetime.now()

def scheduler_api():
    print("Every 10 seconds this executed")
    print("Now : %s" %timeZone.second)
    print("This is SCHEDULE APPS PROCESSING")
    
    travelers = Traveler.objects.all()
    results = ['accuracy', 'satisfaction', 'influence']
    for traveler in travelers:
        survey = traveler.data["survey"]
        count = 0
        print(f'{traveler}')
        for result in results:
            count = survey[result].count(1) + survey[result].count(2)
            if count > len(survey[result])/2:
                print(f'- {result}: 목표 미달성')
            else:
                print(f'- {result}: 목표 충족')
        
    
