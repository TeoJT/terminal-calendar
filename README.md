# Terminal Calendar

A calendar that displays in a Linux command line terminal where you can add reminders and events with a single command.

# Features:
- Beautiful colorful calendar that displays right in your terminal.
- Events that display just in and below your calendar, and show you info like how long until the event and when it is.
- Notify script that continuously checks upcoming events and sends notifications, to remind you of upcoming events.
- Bash script that allows you to access all of the functionality with just a simple `cal` command.

# Usage:
- Make sure you have created a save.csv file in the root of this project with the following headers:
`name,date,start,end`, followed by a newline
- Run `terminal_calendar.py` to display the calendar and its events.
- Run `add_event.py` to add an event to the csv file. This is the usage of the command:
`python3 add_event.py <name> (date in dd/mm/yyyy format) (start time) (end time)`
Parameters in the () brackets are optional. Leaving them blank will set the event to default values.
E.g.
`python3 add_event.py 'Example event'` creates an event on the current day lasting from 00:00 to 23:59.
For the date parameter, you can use 't' to set the date to tomorrow, or a single digit 1-9 to set the number of days until the event. You can use double digits to set the day in the month (or next month) of the event (for example, `python3 add_event.py 'Event' 09` will add an event on the 9th of this month (or next month if it's already past the 9th in the current month.))

- Use the cal.sh file to create a calendar command and quickly add events! In your `.profile` or `.bashrc` files, create an alias `alias cal="path/to/cal.sh` and then boom, you can access your calendar with the following commands:
    - `cal -h`                                                              show the help menu
    - `cal -a <name> (date in dd/mm/yyyy format) (start time) (end time)`   add an event
    - `cal -d`                                                              display the calendar
    - `cal -u`                                                              undo last added event

- Notify! A script that runs in the background with very low cpu usage that checks events and sends you notifications of upcoming events so that you don't miss a thing. Depending on your distro, add a command to run `python3 notify.py` upon startup. In standard Ubuntu, just go to "Launch applications" and add the command there.


# TODO:
- Add cool screenshot to show off the calendar in this repo
- Improve documentation
- Improve readability of code
- Add bash script to automatically "install" the calendar to terminal.
- Add removeEvent command
- Add other commands like editEvent ect.
- Fix a few unstabilities like events being appended to an already existing line instead of a new line.
- Remove old events from the past to preserve performance when reading the csv file.
- Add a config.json file to customise calendar.
