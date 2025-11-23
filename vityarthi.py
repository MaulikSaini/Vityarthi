from datetime import datetime
import time
from plyer import notification

i = 0

mon = ["Hindi","English","Maths"]
tue = ["Sci...","SSt","IT"]
wed = ["maths","Scie","English"]
thu = ["Hindi","english","maths"]
fri = ["Sci...","SSt","IT"]
sat = ["maths","Scie","English"]

periods = mon

periods_time = ["Time:- 8:00 - 9:00","Time:- 9:30 - 10:30","Time:- 11:00 - 12:00"]

timer = "time to Sci... :- 8:00 - 9:00"


def day(t):
    day = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    return day[t.weekday()]


if __name__ == "__main__":
    while True:
        t = datetime.today()
        day(t)

        if t.hour == 8:
            i = 0
            timer = periods_time[0]
            
        if t.hour == 9 and t.minute == 30:
            i = 1
            timer = periods_time[1]
            
        if t.hour == 11:
            i = 2
            timer = periods_time[2]
        if i == 3:
            break
        if day(t) == 'Monday':
            periods = mon
        
        if day(t) == 'Tuesday':
            periods = tue
        
        if day(t) == 'Wednesday':
            periods = wed
        
        if day(t) == 'Thursday':
            periods = thu
        
        if day(t) == 'Friday':
            periods = fri
        
        if day(t) == 'Saturday':
            periods = sat
        
        if day(t) == 'Sunday':
            notification.notify(title = "Today is Sunday !!!", message = "No Time-Table!!!",timeout = 30,)
            break 
    
        if (i == 0) or (i == 1) or (i == 2):
            notification.notify(title = periods[i], message = timer,timeout = 60,) 
            time.sleep(60*40)

print("Vityarthi")   