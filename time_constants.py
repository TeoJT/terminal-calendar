from datetime import datetime

# DEPRICATED
time = datetime.now()
DAY   = time.day
MONTH = time.month
YEAR  = time.year

HOUR   = time.hour
MINUTE = time.minute
SECOND = time.second

# new
def day():
    return datetime.now().day

def month():
    return datetime.now().month
    
def year():
    return datetime.now().year
    
def hour():
    return datetime.now().hour
    
def minute():
    return datetime.now().minute
    
def second():
    return datetime.now().second
    





# month() = 7
# year() = 2021
