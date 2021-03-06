#!/usr/bin/python
#TODO : parser 로 모듈화하여 main 로직이랑 분리
import os
from datetime import datetime
from pytz import timezone,utc
from mailer import Mailer
from memcached import Memcached
import json

os.system('curl -s "https://www.nike.com/kr/launch/?type=upcoming" | grep 응모 > /tmp/nike_temp.log')

f = open('/tmp/nike_temp.log', 'r')
mailer = Mailer()
memcached = Memcached()
schedule_key = 'nike_schedule'

# TODO : 나이키 드로우 특성상 10시에 드로우 하므로 우선순위가 떨어져 시간에 대한 검증은 하지 않는다 추후 리팩토링 때.. 
now = datetime.now()
kst = timezone('Asia/Seoul')
now = datetime.utcnow()
now = utc.localize(now).astimezone(kst)
month = now.month
day = now.day

send_condition_satisfied = False
need_schedule_save = False
# TODO : 저장소에 들어 있는 예정 정보를 불러와서 메일을 보낼지 말지 판단한다

saved_schedule_info = memcached.get(schedule_key)
if saved_schedule_info is None : saved_schedule_info = {}
else : saved_schedule_info = json.loads(saved_schedule_info)

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
                if date_info[0] not in saved_schedule_info : saved_schedule_info[date_info[0]] = {}
                saved_schedule_info[date_info[0]][date_info[1]] = True
                need_schedule_save = True

f.close()

if send_condition_satisfied == True:
    print('send message')
    receivers = [
        # set mail receivers mail addresses here
    ]
    mailer.send_message(receivers)
    print('send message done')

if need_schedule_save == True:
    memcached.set(schedule_key, json.dumps(saved_schedule_info))