
from datetime import datetime
from datetime import timedelta 

def NowdateTime():
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M")
    return date_time

# def EnddateTime(time):
#     now = datetime.now() + timedelta(seconds= time)  
#     end_date_time = now.strftime("%m/%d/%Y, %H:%M")
#     return end_date_time
