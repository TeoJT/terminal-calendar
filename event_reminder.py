from util import calendar, nextMonth
from time_constants import DAY, MONTH, YEAR, HOUR, MINUTE, SECOND
from events_loader import searchEvent
from colors import colors
from EventRecord import EventRecord
from datetime import datetime

EVENTS_DISPLAY_RANGE  = 5
EVENTS_DISPLAY_LENGTH = 50


def getUpcomingEvents(dayRange):
    currentDay = DAY
    currentMonth = MONTH
    currentYear = YEAR

    eventsList = []
    daysInMonth = calendar.monthrange(YEAR, currentMonth)[1]
    for i in range(0, dayRange, 1):
        day = currentDay+i
        eventsList += [searchEvent(day, currentMonth, currentYear)]
        #print(searchEvent(day, currentMonth, currentYear))
        if (day > daysInMonth):
            currentDay = -i+1
            currentMonth = nextMonth(currentMonth)
            if (currentMonth == 1):
                currentYear += 1 
            daysInMonth = calendar.monthrange(currentYear, currentMonth)[1]
    return eventsList

def getTimeUntil(e):
    #Get the date and time
    dt = e.getDate()
    tt = e.getStart()

    #Use the date and time to get the future
    future = datetime(dt.getYear(), dt.getMonth(), dt.getDay(), tt.getHour(), tt.getMin(), 00)

    #Use the current time to get the current time
    now = datetime(YEAR, MONTH, DAY, HOUR, MINUTE, SECOND)

    #And get the time between the future and the current date.
    dur = int((future-now).total_seconds())

    #Get the days, hours, and minutes remaining until that event.
    #(3600 seconds in an hour, 60 seconds in a minute)
    daysUntil    = int(dur / (3600*24))
    dur -= (3600*24)*daysUntil
    hoursUntil   = int(dur / 3600)
    dur -= 3600*hoursUntil
    minutesUntil = int(dur/60)

    return daysUntil, hoursUntil, minutesUntil

def generateHeader(headerText, e):
    display = headerText + e.getName()
    whitespace = "⠀" * (EVENTS_DISPLAY_LENGTH-len(display))
    return display+whitespace


def displayEvent(e):
    daysUntil, hoursUntil, minutesUntil = getTimeUntil(e)

    #Header
    if (daysUntil == 0):
        print(colors.EVENT_NOW + generateHeader("TODAY: ",e) + colors.NONE)
    elif (daysUntil < 2):
        print(colors.EVENT_SOON+ generateHeader("SOON: ",e) + colors.NONE)
    else:
        print(colors.EVENT_UPCOMING + generateHeader("UPCOMING: ",e) + colors.NONE)

    #Date and time
    print(e.getDate().getDate() + "   " + e.getStart().getTime()+" - "+e.getEnd().getTime())
    
    #How long until it is until the event
    if (minutesUntil < 0 or hoursUntil < 0 or daysUntil < 0):
        print(colors.GOLD+colors.UNDERLINE+"ON NOW!"+colors.NONE)
    elif (daysUntil == 0):
        print(colors.RED+str(hoursUntil)  + " hours, " + str(minutesUntil) + " minutes"+colors.NONE)
    elif (daysUntil < 2):
        print(colors.PURPLE+str(daysUntil)  + " day, " + str(hoursUntil) + " hours, " + str(minutesUntil) + " minutes"+colors.NONE)
    else:
        print(colors.WHITE+str(daysUntil) + " days"+colors.NONE)

    print()

#Display all events within a certain time range.
def displayUpcomingEvents(dayRange):
    eventDays = getUpcomingEvents(dayRange)
    for event in eventDays:
        for e in event:
            displayEvent(e)
