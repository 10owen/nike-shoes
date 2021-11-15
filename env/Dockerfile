FROM frolvlad/alpine-python3

RUN apk update
RUN apk add --no-cache bash
RUN apk add --no-cache curl
RUN apk add --no-cache tini
ENTRYPOINT ["/sbin/tini", "--"]
CMD ["/usr/sbin/crond", "-f"]
ENV SENDER_EMAIL=sender_eamil@sender.net
ENV SENDER_PW=sender_eamil_password

RUN pip install pytz
COPY ./env/crontab.sh /home/nike/crontab.sh
RUN sh /home/nike/crontab.sh