import csv
import os
from TimeRecord import TimeRecord
from DateRecord import DateRecord
from EventRecord import EventRecord
from time_constants import DAY, MONTH, YEAR

CSV_FILENAME = os.path.dirname(__file__)+"/save.csv"
FIELDNAMES = ["name", "date", "start", "end"]

eventDay = dict()

def searchEvent(day, month, year):
    #convert the numerical date values to string and search the dictionary
    try:
        e = eventDay[DateRecord().setDate(day, month, year).getDate()]
        return e
    except:
        return []

def newCSV():
    file = open(CSV_FILENAME, "w")
    csvWriter = csv.DictWriter(file, fieldnames=FIELDNAMES)
    file.close()


def addToCSV(row):
    file = open(CSV_FILENAME, "a")
    csvWriter = csv.DictWriter(file, fieldnames=FIELDNAMES)
    #csvWriter.writeheader()
    csvWriter.writerow(row)
    file.close()

def deleteRow(row):
    with open(CSV_FILENAME, "r") as f:
        lines = f.readlines()
    with open(CSV_FILENAME, "w") as f:
        for line in lines:
            if line.strip("\n") != row:
                f.write(line)
    f.close()
        





#Loads everything into the variable eventDay
def loadFromCSV():
    file = open(CSV_FILENAME, "r")
    csvReader = csv.DictReader(file)

    for row in csvReader:
        event = EventRecord(row["name"],
                DateRecord().setFromString(row["date"]), 
                TimeRecord().setFromString(row["start"]), 
                TimeRecord().setFromString(row["end"]))
            
        d = row["date"] #DateRecord().setFromString(row["date"]).getDate()
        try:
            e = eventDay[d]
            eventDay[d].append(event)
        except:
            eventDay[d] = [event]
    

#Test add record
def testSavingRecord():
    # name  =  "terncode is horny"
    # date  =  DateRecord().setDate(DAY()+1, MONTH(), YEAR())
    # start =  TimeRecord().setTime(11, 30)
    # end   =  TimeRecord().setTime(12, 00)
    # record = {"name":name, "date":date.getDate(), "start":start.getTime(), "end":end.getTime()}
    addToCSV({"name":"terncodee", "date":"02/11/2021", "start":"11:00", "end":"12:00"})