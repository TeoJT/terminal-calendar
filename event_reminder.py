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
            daysInMonth = calendar.monthrange(YEAR, currentMonth)[1]
    return eventsList

def getTimeUntil(e):
    dt = e.getDate()
    tt = e.getStart()
    future = datetime(dt.getYear(), dt.getMonth(), dt.getDay(), tt.getHour(), tt.getMin(), 00)
    now = datetime(YEAR, MONTH, DAY, HOUR, MINUTE, SECOND)
    dur = int((future-now).total_seconds())

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

def displayUpcomingEvents():
    eventDays = getUpcomingEvents(EVENTS_DISPLAY_RANGE)
    for event in eventDays:
        for e in event:
            daysUntil, hoursUntil, minutesUntil = getTimeUntil(e)

            #Header
            if (daysUntil == 0):
                print(colors.EVENT_NOW + generateHeader("TODAY: ",e) + colors.NONE)
            elif (daysUntil < 3):
                print(colors.EVENT_SOON+ generateHeader("SOON: ",e) + colors.NONE)
            else:
                print(colors.EVENT_UPCOMING + generateHeader("UPCOMING: ",e) + colors.NONE)

            #Date and time
            print(e.getDate().getDate() + "   " + e.getStart().getTime()+" - "+e.getEnd().getTime())
            
            #How long until it is until the event
            if (daysUntil == 0):
                print(colors.RED+str(hoursUntil)  + " hours, " + str(minutesUntil) + " minutes"+colors.NONE)
            elif (daysUntil < 3):
                print(colors.PURPLE+str(daysUntil)  + " days, " + str(hoursUntil) + " hours, " + str(minutesUntil) + " minutes"+colors.NONE)
            else:
                print(colors.BLUE+str(daysUntil) + " days"+colors.NONE)

            print()
