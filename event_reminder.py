from util import calendar, getDaysInMonth, nextMonth
from time_constants import DAY, MONTH, YEAR, HOUR, MINUTE, SECOND
from events_loader import searchEvent
from colors import colors
from EventRecord import EventRecord
from datetime import datetime

EVENTS_DISPLAY_RANGE  = 7
EVENTS_DISPLAY_LENGTH = 50


def getUpcomingEvents(dayRange):
    currentDay = DAY
    currentMonth = MONTH
    currentYear = YEAR

    eventsList = []
    daysInMonth = getDaysInMonth(currentMonth,YEAR)
    for i in range(1, dayRange, 1):
        day = currentDay+i-1
        eventsList += [searchEvent(day, currentMonth, currentYear)]
        #print(searchEvent(day, currentMonth, currentYear))
        if (day > daysInMonth):
            currentDay = -i+1
            currentMonth = nextMonth(currentMonth)
            if (currentMonth == 1):
                currentYear += 1 
            daysInMonth = getDaysInMonth(currentMonth, currentYear)
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
    if (e.getDate().getDay() == DAY):
        print(colors.EVENT_NOW + generateHeader("TODAY: ",e) + colors.NONE)
    elif (daysUntil == 0):
        print(colors.EVENT_SOON+ generateHeader("TOMORROW: ",e) + colors.NONE)
    elif (daysUntil < 0 or hoursUntil < 0 or minutesUntil < 0):
        print(colors.EVENT_ENDED + generateHeader("ENDED: ",e) + colors.NONE)
    elif (daysUntil < 2):
        print(colors.EVENT_SOON+ generateHeader("SOON: ",e) + colors.NONE)
    else:
        print(colors.EVENT_UPCOMING + generateHeader("UPCOMING: ",e) + colors.NONE)

    #Date and time
    print(e.getDate().getDate() + "   " + e.getStart().getTime()+" - "+e.getEnd().getTime())
    #d = ""
    
    #How long until it is until the event
    if ((minutesUntil < 0 or hoursUntil < 0) and e.getDate().getDay() == DAY):
        print(colors.GOLD+colors.UNDERLINE+"ON NOW!"+colors.NONE)
    elif (daysUntil < 0 or hoursUntil < 0 or minutesUntil < 0):
        print(colors.GREY+"Past event."+colors.NONE)
    elif (e.getDate().getDay() == DAY):
        print(colors.RED+str(hoursUntil)  + " hours, " + str(minutesUntil) + " minutes"+colors.NONE)
    elif (daysUntil < 2):
        print(colors.PURPLE+str(daysUntil)  + " days, " + str(hoursUntil) + " hours, " + str(minutesUntil) + " minutes"+colors.NONE)
    else:
        print(colors.WHITE+str(daysUntil) + " days"+colors.NONE)

    eventPassed = False
    if ((daysUntil < 0 or hoursUntil < 0 or minutesUntil < 0) and e.getDate().getDay() != DAY):
        print(colors.BOLD+colors.GOLD+"WARNING: This event is set in the past, you should make sure the time is correct."+colors.NONE)
        eventPassed = True
    print()
    return eventPassed

#Display all events within a certain time range.
def displayUpcomingEvents(eventRange=EVENTS_DISPLAY_RANGE):
    eventDays = getUpcomingEvents(eventRange)
    for event in eventDays:
        for e in event:
            if (e.getDate().getDay() == DAY):
                if (HOUR <= e.getEnd().getHour() ):
                    displayEvent(e)
            else:
               displayEvent(e)
