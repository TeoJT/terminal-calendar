
from DateRecord import DateRecord
from EventRecord import EventRecord
from TimeRecord import TimeRecord
from events_loader import CSV_FILENAME, deleteRow
from colors import colors
from error_display import displayError


def deleteEvent(name, date, start, end):
    if (type(date) == DateRecord and type(start) == TimeRecord and type(end) == TimeRecord):
        deleteRow(name+","+date.getDate()+","+start.getTime()+","+end.getTime())
    else:
        deleteRow(name+","+date+","+start+","+end)

def undoEvent():
    with open(CSV_FILENAME, 'r') as f:
        lines = f.read().splitlines()
        last_line = lines[-1]
    if (len(lines) <= 2):
        displayError("There are no events to remove!")
    else:
        deleteRow(last_line)
        print(colors.WHITE+colors.BOLD+"Undid and removed event: "+last_line+"."+colors.NONE)
    f.close()

undoEvent()