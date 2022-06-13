import datetime
from re import M
import sched, time

from DateRecord import DateRecord
from EventRecord import EventRecord
from event_reminder import getTimeUntil, getUpcomingEvents
from events_loader import loadFromCSV
import notify2
from time_constants import HOUR, DAY, MINUTE, SECOND

# index 0 contains 
notifLvl = dict()
CHECK_INTERVAL = 60

def sendNotif(title, message):
    notify2.init("terminal-calendar")
    notice = notify2.Notification(title, message)
    notice.show()
    return


def sendNotifEvent(title, event):
    daysUntil, hoursUntil, minutesUntil = getTimeUntil(event)

    # Make sure our plurals grammer is correct
    mdis = " minute"
    hdis = " hour"
    if (hoursUntil != 1):
        hdis += 's'
    if (minutesUntil != 1):
        mdis += 's'

    # Generate the message. It should look something like this:
    # --Title--
    # Event
    # xx/xx/xx   xx:xx - xx:xx  (x hours, x minutes)
    
    message = (event.getName()+
    "\n"+event.getDate().getDate()+
    "   "+event.getStart().getTime()+
    " - "+event.getEnd().getTime())

    # Add a little extra string showing specifically how much time until the event.
    # We ignore that if the event is already happening now
    if not((minutesUntil < 0 or hoursUntil < 0) and event.getDate().getDay() == DAY()):
        message += "   "+str(hoursUntil)+hdis+", "+str(minutesUntil)+mdis+""

    sendNotif(title, message)



def checkUpcomingEvents():
    loadFromCSV()

    notifsSent = 0
    
    # Just so syntax suggestions actually show up god damn python
    e: EventRecord

    # for some reason this needs to be 3 even though we're only checking today and tomorrow.
    eventDays = getUpcomingEvents(3)
    for event in eventDays:
        for e in event:
            if (notifsSent <= 3):
                # Here we send the upcoming notifications

                daysUntil, hoursUntil, minutesUntil = getTimeUntil(e)

                # Get the notification level
                # Of course we can't access the level from the event object,
                # so we'll use that whole "turning a memory address into a string that
                # is also an address to a dict" hack.

                # added note: id is going to be different each time we keep re-loading
                # the csv file and i can't be bothered to come up with an elegant solution
                # so I'm just gonna hash the name for now and use that as an address
                try:
                    level = notifLvl[hex(hash(e.getName()))]
                    print(e.getName()+" "+str(hoursUntil)+" "+str(minutesUntil)+" get level   "+str(level))
                except:
                    level = 0

                # Each event, when get sent as a notification, is assigned a level.
                # This is to prevent the notification being sent already, but if it changes
                # state due to time, e.g. "Less than an hour" to "Less than 30 mins", the event
                # notification advances a level up so that its new message can be sent.
                
                if (e.getDate().getDay() == DAY()):

                    # Within minutes or an hour(s)
                    if ((minutesUntil < 0 or hoursUntil < 0)) and level < 10:
                        sendNotifEvent("Event on now!", e)
                        level = 10
                        notifsSent += 1
                    elif (hoursUntil == 0 and minutesUntil == 1) and level < 9:
                        sendNotifEvent("Event in a min!", e)
                        level = 9
                        notifsSent += 1
                    elif (hoursUntil == 0 and minutesUntil <= 30) and level < 9:
                        sendNotifEvent("Event in "+str(minutesUntil)+" mins!", e)
                        level = 9
                        notifsSent += 1
                    elif (hoursUntil == 0 and minutesUntil <= 59) and level < 8:
                        sendNotifEvent("In less than an hour!", e)
                        level = 8
                        notifsSent += 1
                    elif (hoursUntil <= 2 and minutesUntil <= 59) and level < 7:
                        sendNotifEvent("Soon", e)
                        level = 7
                        notifsSent += 1
                    elif (level < 6):
                        sendNotifEvent("Today", e)
                        level = 6
                        notifsSent += 1
                        
                        
                elif (daysUntil == 0) and level < 5:
                    sendNotifEvent("Tomorrow", e)
                    level = 5
                    notifsSent += 1

                # Note that we're just starting from 10 and decending down.
                # It doesn't really matter that the minimum level is 5.

                # Update level.
                notifLvl[hex(hash(e.getName()))] = level
                print(e.getName()+" "+str(hoursUntil)+" "+str(minutesUntil)+" "+e.getStart().getTime()+" set level   "+str(level))



# --- Begin our program here ---
checkUpcomingEvents()

# this code over there runs a background process that executes a check every minute.

s = sched.scheduler(time.time, time.sleep)
def do_something(sc): 
    #print("Doing stuff...")
    # do your stuff
    print("Doing check")
    checkUpcomingEvents()

    sc.enter(CHECK_INTERVAL, 1, do_something, (sc,))

s.enter(CHECK_INTERVAL, 1, do_something, (s,))
s.run()


