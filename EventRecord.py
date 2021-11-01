from util import digitalTimeFormat

class EventRecord:
    def __init__(self, name, date, start, end) -> None:
        self.name  = name
        self.date  = date
        self.start = start
        self.end   = end

    def getName(self):
        return self.name

    def getDate(self):
        return self.date

    def getStart(self):
        return self.start

    def getEnd(self):
        return self.end