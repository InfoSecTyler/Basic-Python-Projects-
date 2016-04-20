'''
Created by: Tyler Linne
Coded in part as a Treehouse Project
Date: 4-20-16
'''

from datetime import datetime

import pytz

OTHER_TIMEZONES = [
    pytz.timezone('US/Eastern'),
    pytz.timezone('US/Mountain'),
    pytz.timezone('US/Pacific'),
    pytz.timezone('Pacific/Auckland'),
    pytz.timezone('Asia/Calcutta'),
    pytz.timezone('UTC'),
    pytz.timezone('Europe/Paris'),
    pytz.timezone('Africa/Khartoum')
]
fmt = '%m-%d-%Y %H:%M:%S %Z%z'

while True:
    date_input = input("""When is your meeting?
-Please use MM/DD/YYYY HH:MM format- 
""")
    try:
        local_date = datetime.strptime(date_input, '%m/%d/%Y %H:%M')
    except ValueError:
        print("{} doesn't seem to be a valid date & time.".format(date_input))
    else:
        local_date = pytz.timezone('US/Mountain').localize(local_date)
        utc_date = local_date.astimezone(pytz.utc)
        
        output = []
        for timezone in OTHER_TIMEZONES:
            output.append(utc_date.astimezone(timezone))
        for appointment in output:
            print('-'*20)
            print(appointment.strftime(fmt))
        break