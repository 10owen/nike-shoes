#!/usr/bin/python
import os
from datetime import datetime
from pytz import timezone,utc
from mailer import Mailer

os.system('curl -s "https://www.nike.com/kr/launch/?type=upcoming" | grep 응모 > /tmp/nike_temp.log')

f = open('/tmp/nike_temp.log', 'r')
mailer = Mailer()

# TODO : 나이키 드로우 특성상 10시에 드로우 하므로 우선순위가 떨어져 시간에 대한 검증은 하지 않는다 추후 리팩토링 때.. 
now = datetime.now()
kst = timezone('Asia/Seoul')
now = datetime.utcnow()
now = utc.localize(now).astimezone(kst)
month = now.month
day = now.day

send_condition_satisfied = False

while True:
    line = f.readline()
    if not line: break
    if "available-date-component" in line and "응모" in line:
        if "응모하기" in line:
            send_condition_satisfied = True
            break;
        line = line.strip()
        start = line.find(">")
        end = line.rfind("<")
        draw_info = line[start+1:end]
        print(draw_info)

        draw_info = draw_info.split()
        for di in draw_info:
            if "/" in di:
                date_info = di.split("/")
                if(int(date_info[0]) == month and int(date_info[1]) == day):
                    # TODO : db에 저장할까?
                    pass
f.close()

if send_condition_satisfied == True:
    print('send message')
    receivers = [
        # set mail receivers mail addresses here
    ]
    mailer.send_message(receivers)
    print('send message done')

