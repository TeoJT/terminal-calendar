from colors import colors
from util import combine, getDaysInMonth, prevMonth, nextMonth, cal, calendar, getMonthName
from time_constants import DAY, MONTH, YEAR
from events_loader import searchEvent

def getEventLine(line, otherMonth):

    x = []
    for i in range(len(line[0])):
        if (line[1][i]):
            e = searchEvent(line[0][i], MONTH, YEAR)
        else:
            e = searchEvent(line[0][i], otherMonth, YEAR)
        x += [e]
    return x
            

def displayLine(line, event, months):
    lineStr = ""
    x = tuple(zip(line, event, months))
    for i in x:
        space = " "
        if (i[0] < 10):
            space = "  "
        
        if (i[0] == DAY):
            col = colors.HIGHLIGHT
        elif (not i[2]):
            col = colors.GREY
        else:
            col = colors.WHITE
        
        if (len(i[1]) == 1):
            if (i[0] == DAY):
                col = colors.BLACK+colors.HYELLOW
            else:
                col = colors.GOLD
        elif (len(i[1]) > 1):
            if (i[0] == DAY):
                col = colors.BLACK+colors.HRED
            else:
                col = colors.LRED

        lineStr += (col + str(i[0]) + colors.NONE + space + colors.NONE)

    print(lineStr)



def displayCalendar():
    #find the line that contains today's day.
    index = 0
    for line in cal:
        if DAY in line:
            break
        index = index + 1
    
    thisMonthsCal = []
    for i in range(len(cal)):
        thisMonthsCal += [[True, True, True, True, True, True, True]]

    #Days outside of the m
    #There's a buncha 0's at the beginning of the calendar month
    prevInterval = 0
    if (0 in cal[0]):
        otherMonth = calendar.monthcalendar(YEAR, prevMonth())
        combine(cal[0], otherMonth[len(otherMonth)-1], thisMonthsCal[0])
        prevInterval = 1
    #There's a buncha 0's at the end of the calendar month
    nextInterval = 0
    if (0 in cal[len(cal)-1]):
        otherMonth = calendar.monthcalendar(YEAR, nextMonth())
        combine(cal[len(cal)-1], otherMonth[0], thisMonthsCal[len(thisMonthsCal)-1])
        nextInterval = 1

    
    calTuple = tuple(zip(cal, thisMonthsCal))



    #Early in the month
    if (line is calTuple[0][0]):
        otherMonth = calendar.monthcalendar(YEAR, prevMonth())
        nextLine = calTuple[1]
        line     = calTuple[index]
        prevLine = (otherMonth[len(otherMonth)-1-prevInterval], [False]*7)
    #Late in the month
    elif (line is calTuple[len(cal)-1][0]):
        otherMonth = calendar.monthcalendar(YEAR, nextMonth())
        prevLine = calTuple[index-1]
        line     = calTuple[index]
        nextLine = (otherMonth[nextInterval], [False]*7)
    #Somewhere in the middle of the month
    else:
        prevLine = calTuple[index-1]
        line     = calTuple[index]
        nextLine = calTuple[index+1]

    #get list of events in the calendar
    prevEventLine = getEventLine(prevLine, prevMonth())

    if (DAY <= 7):
        presentEventLine = getEventLine(line, prevMonth())
    elif (DAY >= getDaysInMonth(MONTH, YEAR)-7):
        presentEventLine = getEventLine(line, nextMonth())
    else:
        presentEventLine = getEventLine(line, MONTH)

    nextEventLine = getEventLine(nextLine, 12)


    #Actually display the calendar
    print(colors.CYAN + colors.UNDERLINE
                   + str(DAY) + " " 
                   + getMonthName(MONTH) 
                   + " " + str(YEAR) 
                   + colors.NONE)
    print(colors.GREY + "Mo Tu We Th Fr Sa Su" + colors.NONE)
    displayLine(prevLine[0], prevEventLine,  prevLine[1])
    displayLine(line[0],     presentEventLine,  line[1])
    displayLine(nextLine[0], nextEventLine, nextLine[1])
    print()


