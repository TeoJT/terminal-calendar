from events_loader import addToCSV
from time_constants import DAY, MONTH, YEAR


def addEvent(name, date, start="00:00", end="23:59"):
    if (date == "t"):
        date = str(DAY+1)
    addToCSV({"name":name, "date":date, "start":start, "end":end})