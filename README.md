# Terminal Calendar

A calendar that displays in a Linux command line terminal where you can add reminders and events with a single command.

# Usage:
- Make sure you have created a save.csv file in the root of this project with the following headers:
`name,date,start,end`
- Run `terminal_calendar.py` to display the calendar and its events.
- Run `add_event.py` to add an event to the csv file. This is the usage of the command:
`python3 add_event.py <name> (date in dd/mm/yyyy format) (start time) (end time)`
Parameters in the () brackets are optional. Leaving them blank will set the event to default values.
E.g.
`python3 add_event.py 'Example event'` creates an event on the current day lasting from 00:00 to 23:59.
For the date parameter, you can use 't' to set the date to tomorrow, or a single digit 1-9 to set the number of days until the event. You can use double digits to set the day in the month (or next month) of the event (for example, `python3 add_event.py 'Event' 09` will add an event on the 9th of this month (or next month if it's already past the 9th in the current month.))

- Optionally you can use the bash scripts in the bash folder to display the calendar every time you start up the terminal. Make sure to set the correct location of the python files in the bash scripts first. On the root directory open the aliases file using `nano .bash_aliases` and append the following to the file:
`alias addEvent='. ~/addEvent.sh'`
`alias calendar='. ~/calendar.sh'`
`calendar`

Close the file with ctrl+X and then restart your terminal. You should now see the calendar display whenever yous tart up the file. You can also now use `addEvent 'Event'` instead of `python3 add_event.py 'Event`

# TODO:
- Improve documentation
- Improve readability of code
- Add bash script to automatically "install" the calendar to terminal.
- Add removeEvent command
- Add other commands like editEvent ect.
- Fix a few unstabilities like events being appended to an already existing line instead of a new line.
- Remove old events from the past to preserve performance when reading the csv file.
- Add a config.json file to modify configurations.
