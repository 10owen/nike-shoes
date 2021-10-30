#!/bin/bash

#write out current crontab
crontab -l > mycron
#echo new cron into cron file
echo "* * * * * python /home/nike/nike-shoes/module/parse.py >> /tmp/test.log" >> mycron
#install new cron file
crontab mycron
rm mycron