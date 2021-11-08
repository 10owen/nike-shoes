#!/usr/bin/python

import requests
import os
from datetime import datetime
# os.system('curl -s "https://www.nike.com/kr/launch/?type=upcoming"  > /tmp')
os.system('curl -s "https://www.nike.com/kr/launch/?type=upcoming" | grep 응모 > /tmp/nike_temp.log')

f = open('/tmp/nike_temp.log', 'r')
month = datetime.now().month
day = datetime.now().day

while True:
    line = f.readline()
    if not line: break
    if "available-date-component" in line and "응모" in line:
        print(line)
        line = line.strip()
        start = line.find(">")
        end = line.rfind("<")
        draw_info = line[start+1:end]
        print(draw_info)

        draw_info = draw_info.split()
        for di in draw_info:
            if "/" in di:
                date_info = di.split("/")
                if(int(date_info[0]) == month and int(date_info[1]) != day):
                    print("bingo!!")
        
f.close()