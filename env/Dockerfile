FROM frolvlad/alpine-python3

RUN apk update
RUN apk add --no-cache bash
RUN pip install requests
COPY ./env/crontab.sh /home/nike/crontab.sh
RUN sh /home/nike/crontab.sh