import sys
from event_reminder import displayUpcomingEvents
from events_loader import loadFromCSV


loadFromCSV()
displayUpcomingEvents(int(sys.argv[1]))