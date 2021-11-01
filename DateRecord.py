from util import digitalTimeFormat

class DateRecord:

    def __init__(self) -> None:
        self.day    = 0
        self.month  = 0
        self.year   = 0

    def setFromString(self, string):
        self.day    = int(string[0:2])
        self.month  = int(string[3:5])
        self.year   = int(string[6:10])
        return self

    def setDate(self, day, month, year):
        self.day    = day
        self.month  = month
        self.year   = year
        return self

    def getDay(self):
        return self.day

    def getMonth(self):
        return self.month

    def getYear(self):
        return self.year

    def getDate(self):
        return digitalTimeFormat(self.getDay())+"/"+digitalTimeFormat(self.getMonth())+"/"+str(self.getYear())
