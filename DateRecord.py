from InvalidData import InvalidData
from util import digitalTimeFormat, getDaysInMonth

class DateRecord:

    def __init__(self) -> None:
        self.day    = 0
        self.month  = 0
        self.year   = 0

    def setFromString(self, string):
        try:
            if (len(string) == 8):
                self.day    = int(string[0:2])
                self.month  = int(string[3:5])
                self.year   = 2000+int(string[6:8])
            else:
                self.day    = int(string[0:2])
                self.month  = int(string[3:5])
                self.year   = int(string[6:10])
        except ValueError:
            raise InvalidData

        if (self.year < 2000 or self.year > 9999):
            raise InvalidData

        if (self.month < 1 or self.month > 12):
            raise InvalidData

        if (self.day < 1 or self.day > getDaysInMonth(self.month, self.year)):
            raise InvalidData
            
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
