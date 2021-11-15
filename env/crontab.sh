#!/bin/bash

#write out current crontab
crontab -l > mycron
#echo new cron into cron file
echo "5 1 * * * python /home/nike/nike-shoes/module/parse.py >> /tmp/test.log" >> mycron
#install new cron file
crontab mycron
rm mycron