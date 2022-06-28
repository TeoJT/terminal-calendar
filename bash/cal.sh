#!/bin/sh

calLoc="$MYDATA_PROJECTS/terminal-calendar"
if [ -f "$calLoc/terminal_calendar.py" ]; then
	if [ "$1" = "" ] || [ "$1" = "-d" ]; then
		python3 "$calLoc/terminal_calendar.py"
	elif [ "$1" = "-h" ] || [ "$1" = "help" ] || [ "$1" = "-help" ]; then
		echo "terminal-calendar bash usage:"
		echo "-h     show this help menu"
		echo "-d     display the calendar"
		echo '-a     add event, followed by <event name> <day> <start time> <end time>'
		echo '-u     undo add event'
	elif [ "$1" = "-a" ]; then
		pyPath="$calLoc/add_event.py"
		if ! [ -z "$5" ]; then
		python3 "$pyPath" "$2" "$3" "$4" "$5"
	elif ! [ -z "$4" ]; then
		python3 "$pyPath" "$2" "$3" "$4"
	elif ! [ -z "$3" ]; then
		python3 "$pyPath" "$2" "$3" 
	elif ! [ -z "$2" ]; then
		python3 "$pyPath" "$2"
		else
			python3 "$pyPath"
		fi
	elif [ "$1" = "-u" ]; then
		python3 "$calLoc/undo_event.py"
	else
		echo "Unknown operator $1"
	fi
else
	tput setaf 1; echo "Warning: terminal-calendar not found. You should update the location set in this bash script."
fi
