from datetime import datetime
import calendar

time = datetime.now()
#colors.dispAll()

#Get the weeks of the month, which contain the days of the month
cal = calendar.monthcalendar(time.year, time.month)

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

def prevMonth(startingMonth = time.month):
    month = startingMonth-1
    if (month < 1):
        month = 12
    return month

def nextMonth(startingMonth = time.month):
    month = startingMonth+1
    if (month > 12):
        month = 1
    return month

def replaceAll(list, oldItem, newItem):
    for i in range(len(list)):
        if (list[i] == oldItem):
            list[i] = newItem
    
def combine(list1, list2):
    for i in range(len(list1)):
        if (list1[i] == 0):
            list1[i] = list2[i]
        