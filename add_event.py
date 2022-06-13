#!/usr/bin/python

import sys
from DateRecord import DateRecord
from EventRecord import EventRecord
from InvalidData import InvalidData
from TimeRecord import TimeRecord
from colors import colors
from error_display import displayError
from event_reminder import displayEvent
from events_loader import addToCSV
from time_constants import DAY, MONTH, YEAR
from util import digitalTimeFormat, processDay
import copy

def setDay(day, month, year):
    return digitalTimeFormat(day)+"/"+digitalTimeFormat(month)+"/"+str(year)

def confirm(message):
    response = ""
    while (response.lower() != "y" and response.lower() != "n"):
        response = input(message)
    if (response.lower() == "y"):
        return True
    else:
        return False


def addEvent(name, date, start, end):
    
    if (name.find(",") != -1 or date.find(",") != -1 or start.find(",") != -1 or end.find(",") != -1 ):
        displayError("There must be NO commas in the event's name date and times!")
        return


    nameIsDate = True
    for c in name:
        if ((ord(c) >= ord('0') and ord(c) <= ord('9')) or (ord(c) == ord('/'))) == False:
            nameIsDate = False

    if (nameIsDate):
        if (confirm("I think you forgot to add the name. Do you want to enter a name now? y/n\n")):
            if (end != "23:59"):
                end = copy.copy(start)
            if (end != "00:00"):
                start = copy.copy(date)
            date = copy.copy(name)
            name = input("Enter new name:\n")
    
    month = MONTH()
    year = YEAR()
    if (date == "today"):
        day = DAY()
        date = setDay(day, month, year)
    elif (date == "t" or date == "tomorrow"):
        day, month, year = processDay(DAY()+1, MONTH(), YEAR())
        date = setDay(day, month, year)
    elif (len(date) == 1):
        day, month, year = processDay(DAY()+int(date), MONTH(), YEAR())
        date = setDay(day, month, year)
    elif (len(date) == 2):
        day = int(date)
        if (day < DAY()):
            day, month, year = processDay(day, MONTH()+1, YEAR())
        date = setDay(day, month, year)
    


    passChecks = True

    try:
        d = DateRecord().setFromString(date)
    except InvalidData:
        d = None
        passChecks = False
        displayError("Impossible date, you might want to check that again...")

    if (passChecks):
        try:
            s = TimeRecord().setFromString(start)
        except InvalidData:
            s = None
            passChecks = False
            displayError("Impossible start time, you might want to check that again...")

    if (passChecks):
        try:
            e = TimeRecord().setFromString(end)
        except InvalidData:
            e = None
            passChecks = False
            displayError("Impossible end time, you might want to check that again...")

    if passChecks:
        event = EventRecord(name,
                    d, 
                    s, 
                    e)
        print(colors.BOLD+"Event added: "+colors.NONE)

        #Check if event is in the past.
        IN_THE_PAST = True
        if (displayEvent(event) == IN_THE_PAST):
            if (confirm("This event is set in the past.\nAre you sure you set the right date/time? y/n\n")):
                print(colors.GOLD+"Add event cancelled."+colors.NONE)
                return


            
        addToCSV({"name":name, "date":date, "start":start, "end":end})


l = len(sys.argv)-1
arg1 = str(sys.argv[1])

if (l == 0):
    displayError("No arguments provided.")
elif (l == 1):
    addEvent(arg1, "today", "00:00", "23:59")
elif (l == 2):
    addEvent(str(sys.argv[1]), str(sys.argv[2]), "00:00", "23:59")
elif (l == 3):
    addEvent(str(sys.argv[1]), str(sys.argv[2]), str(sys.argv[3]), "23:59")
elif (l == 4):
    addEvent(str(sys.argv[1]), str(sys.argv[2]), str(sys.argv[3]), str(sys.argv[4]))