#!/usr/bin/python

import sys
from DateRecord import DateRecord
from EventRecord import EventRecord
from TimeRecord import TimeRecord
from colors import colors
from event_reminder import displayEvent
from events_loader import addToCSV
from time_constants import DAY, MONTH, YEAR
from util import digitalTimeFormat, processDay

def setDay(day, month, year):
    return digitalTimeFormat(day)+"/"+digitalTimeFormat(month)+"/"+str(year)

def addEvent(name, date="today", start="00:00", end="23:59"):
    if (len(start) == 0):
        start="00:00"
    if (len(end) == 0):
        end="23:59"
    #if (name[0] == '\'' or name[0] == '"'):
    #    name[0] = ''
    #if (name[-1] == '\'' or name[-1] == '"'):
    #    name[-1] = ''
    
    month = MONTH
    year = YEAR
    if (date == "today"):
        day = DAY
        date = setDay(day, month, year)
    elif (date == "t" or date == "tomorrow"):
        day, month, year = processDay(DAY+1, MONTH, YEAR)
        date = setDay(day, month, year)
    elif (len(date) == 1):
        day, month, year = processDay(DAY+int(date), MONTH, YEAR)
        date = setDay(day, month, year)
    elif (len(date) == 2):
        day = int(date)
        if (day < DAY):
            day, month, year = processDay(day, MONTH+1, YEAR)
        date = setDay(day, month, year)
    else:
        day = DAY
        date = setDay(day, month, year)
    
    addToCSV({"name":name, "date":date, "start":start, "end":end})
    event = EventRecord(name,
                DateRecord().setFromString(date), 
                TimeRecord().setFromString(start), 
                TimeRecord().setFromString(end))
    print(colors.BOLD+"Event added: "+colors.NONE)
    displayEvent(event)

l = len(sys.argv)-1
arg1 = str(sys.argv[1])

if (l == 1):
    addEvent(arg1)
elif (l == 2):
    addEvent(str(sys.argv[1]), str(sys.argv[2]))
elif (l == 3):
    addEvent(str(sys.argv[1]), str(sys.argv[2]), str(sys.argv[3]))
elif (l == 4):
    addEvent(str(sys.argv[1]), str(sys.argv[2]), str(sys.argv[3]), str(sys.argv[4]))