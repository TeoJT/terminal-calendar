#!/bin/sh

myDirStruct="tablop_neonn_F"
if [ "$DIR_STRUCTURE" != "$myDirStruct" ]; then
        tput setaf 1; echo "Dir structure expected to be $myDirStruct but instead is $DIR_STRUCTURE."
        return
fi

python3 /home/neonn/mydata/projects/terminal-calendar/notify.py
