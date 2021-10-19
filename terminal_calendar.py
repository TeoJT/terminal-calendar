from colors import colors
from util import combine, prevMonth, nextMonth, time, cal, calendar, getMonthName

def displayLine(line):
    lineStr = ""
    for i in line:
        space = " "
        if (i < 10):
            space = "  "

        if (i == time.day):
            lineStr += (colors.HIGHLIGHT + str(i) + colors.NONE + space)
        else:
            lineStr += (colors.WHITE + str(i) + space)
    print(lineStr)



def displayCalendar():
    #find the line that contains today's day.
    index = 0
    for line in cal:
        if time.day in line:
            break
        index = index + 1
    
    prevInterval = 0
    if (0 in cal[0]):
        otherMonth = calendar.monthcalendar(time.year, prevMonth())
        combine(cal[0], otherMonth[len(otherMonth)-1])
        prevInterval = 1
    
    nextInterval = 0
    if (0 in cal[len(cal)-1]):
        otherMonth = calendar.monthcalendar(time.year, nextMonth())
        combine(cal[len(cal)-1], otherMonth[0])
        nextInterval = 1


    #Early in the month
    if (line is cal[0]):
        otherMonth = calendar.monthcalendar(time.year, prevMonth())
        nextLine = cal[1]
        prevLine = otherMonth[len(otherMonth)-1-prevInterval]
    #Late in the month
    elif (line is cal[len(cal)-1]):
        otherMonth = calendar.monthcalendar(time.year, nextMonth())
        prevLine = cal[index-1]
        nextLine = otherMonth[nextInterval]
    #Somewhere in the middle of the month
    else:
        prevLine = cal[index-1]
        nextLine = cal[index+1]

    print(colors.CYAN + colors.UNDERLINE
                   + str(time.day) + " " 
                   + getMonthName(time.month) 
                   + " " + str(time.year) 
                   + colors.NONE)
    print(colors.GREY + "Mo Tu We Th Fr Sa Su" + colors.NONE)
    displayLine(prevLine)
    displayLine(line)
    displayLine(nextLine)
    
    # print(prevLine)
    # print(line)
    # print(nextLine)



displayCalendar()