FROM python:3.8-slim-buster
LABEL MAINTAINER=MP

RUN apt-get update && apt-get -y upgrade

RUN apt-get -y install python3-dev default-libmysqlclient-dev build-essential nano vim telnet

RUN apt-get -y install python3-pip  git curl 
RUN pip3 install mysqlclient
RUN pip3 install gunicorn
RUN mkdir /frontpage

WORKDIR /frontpage/

RUN pip3 install coderedcms 

RUN git clone https://github.com/murat-polat/homepage /frontpage

RUN cd homepage


RUN pip3 install -r requirements.txt



EXPOSE 8000


CMD gunicorn --bind=0.0.0.0:8000 --workers 2 --max-requests=1000 homepage.wsgi:application
