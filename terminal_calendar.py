from calendar import c
from calendar_display import displayCalendar
from event_reminder import EVENTS_DISPLAY_LENGTH, displayUpcomingEvents
from events_loader import loadFromCSV, testSavingRecord

loadFromCSV()
displayCalendar()
displayUpcomingEvents(EVENTS_DISPLAY_LENGTH)