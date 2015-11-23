#!/bin/sh

# leave check timestamp
if [ "$1" = "srv" ]
then
	date > /home/ash/domains/$2/releases/workspace/postman/check.log
	FILENAME=/home/ash/domains/$2/releases/workspace/postman/sites.list
else
	date > check.log
	FILENAME=sites.list
fi

cat $FILENAME | while read -r LINE || [[ -n $LINE ]]
do
	if [ "$1" = "srv" ]
	then
		python /home/ash/domains/$2/releases/workspace/postman/main.py --page=$LINE
	else
		python /Users/ash/Sites/postman/main.py --page=$LINE
	fi
done