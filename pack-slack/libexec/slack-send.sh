#!/bin/bash

while getopts "u:c:m:s:" option
do
	case $option in
		c)
			CHANNEL=$OPTARG
			;;
		u)
			SLACKURL=$OPTARG
			;;
		m)
			MSG=$OPTARG
			;;
		s)
			STATE=$OPTARG
			;;
		\?)
			echo "Invalid option"
			exit 1
	esac
done

if [ -z "${SLACKURL}" -o -z "${MSG}" -o -z "${STATE}" ];
then
	echo "Missing parameters"
	exit 1
fi

if [ "$STATE" = "CRITICAL" ]
then
    ICON=":exclamation:"
elif [ "$STATE" = "WARNING" ]
then
    ICON=":warning:"
elif [ "$STATE" = "OK" ]
then
    ICON=":white_check_mark:"
elif [ "$STATE" = "UNKNOWN" ]
then
    ICON=":question:"
elif [ "$STATE" = "UP" ]
then
    ICON=":white_check_mark:"
elif [ "$STATE" = "DOWN" ]
then
    ICON=":exclamation:"
else
    ICON=":white_medium_square:"
fi

FINALMSG=$(echo ${MSG} | sed -r -e "s/\|/\\\n${ICON} /g" -e "s/^/${ICON} /")
if [ -n "${CHANNEL}" ];
then
	FINALCHANNEL="\"channel\": \"${CHANNEL}\","
fi
#DATA="payload={${FINALCHANNEL}\"text\": \"${FINALMSG}\"}"

exec curl -s -X POST --data-urlencode "payload={${FINALCHANNEL}\"text\": \"${FINALMSG}\"}" ${SLACKURL}
