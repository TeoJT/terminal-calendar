from util import digitalTimeFormat

class TimeRecord:

    def __init__(self) -> None:
        self.minutes = 0
        self.hours   = 0

    def setFromString(self, string):
        self.hours = int(string[0:2])
        self.minutes   = int(string[3:5])
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

    