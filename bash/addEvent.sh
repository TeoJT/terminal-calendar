#!/bin/sh

pyPath="/mnt/c/My Data/OneDrive/My Cloud/Projects/git/terminal-calendar/add_event.py"
if ! [ -z "$4" ]; then
	python3 "$pyPath" "$1" "$2" "$3" "$4"
elif ! [ -z "$3" ]; then
	python3 "$pyPath" "$1" "$2" "$3"
elif ! [ -z "$2" ]; then
	python3 "$pyPath" "$1" "$2" 
elif ! [ -z "$1" ]; then
	python3 "$pyPath" "$1"
fi
