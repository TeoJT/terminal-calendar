from InvalidData import InvalidData
from util import digitalTimeFormat

class TimeRecord:

    def __init__(self) -> None:
        self.minutes = 0
        self.hours   = 0

    def setFromString(self, string):
        try:
            self.hours = int(string[0:2])
            self.minutes   = int(string[3:5])
        except ValueError:
            raise InvalidData

        if (self.hours > 23):
            raise InvalidData
        if (self.hours < 0):
            raise InvalidData
        if (self.minutes > 59):
            raise InvalidData
        if (self.minutes < 0):
            raise InvalidData

        return self

    def setTime(self, hr, min):
        self.minutes = min
        self.hours   = hr
        return self

    def getMin(self):
        return self.minutes

    def getHour(self):
        return self.hours

    def getTime(self):
        return digitalTimeFormat(self.getHour())+":"+digitalTimeFormat(self.getMin())

    