import calendar
from time_constants import DAY, MONTH, YEAR

#Get the weeks of the month, which contain the days of the month
cal = calendar.monthcalendar(YEAR, MONTH)

monthNames = ("January",
              "February",
              "March", 
              "April", 
              "May", 
              "June", 
              "July", 
              "August", 
              "September", 
              "October", 
              "November",
              "December")

def getMonthName(index):
    return monthNames[index-1]

def prevMonth(startingMonth = MONTH):
    m = startingMonth-1
    if (m < 1):
        m = 12
    return m

def nextMonth(startingMonth = MONTH):
    m = startingMonth+1
    if (m > 12):
        m = 1
    return m
    
def combine(list1, list2, monthsList = [True]*7):
    for i in range(len(list1)):
        if (list1[i] == 0):
            list1[i] = list2[i]
            monthsList[i] = False

def digitalTimeFormat(n):
    if (n < 10):
        n = "0"+str(n)
    return str(n)

def unpackListOfTuples(list):
    return tuple(zip(*list))

def getDaysInMonth(month, year):
    return calendar.monthrange(year, month)[1]

def processDay(day, month, year):
    daysInMonth = getDaysInMonth(month, year)
    if (day > daysInMonth):
        day -= daysInMonth
        month += 1

    if (month > 12):
        year += 1

    return day, month, year