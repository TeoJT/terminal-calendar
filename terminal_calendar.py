from calendar import c
from calendar_display import displayCalendar
from event_reminder import displayUpcomingEvents
from events_loader import loadFromCSV, testSavingRecord

loadFromCSV()
displayCalendar()
displayUpcomingEvents()