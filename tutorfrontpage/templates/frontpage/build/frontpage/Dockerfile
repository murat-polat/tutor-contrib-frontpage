FROM ubuntu:18.04

LABEL MAINTAINER=MP
RUN apt-get update && apt-get -y upgrade

RUN apt-get -y install python3-dev default-libmysqlclient-dev build-essential nano vim telnet

RUN apt-get -y install python3-pip  git curl 
RUN pip3 install mysqlclient

RUN mkdir /openedx  openedx/frontpage


RUN pip3 install mezzanine uwsgi django==1.8.19

## Here you can add your custom frontpage repository
RUN git clone https://github.com/murat-polat/frontpageapp 

RUN cd /frontpageapp

WORKDIR /frontpageapp

#RUN pip3 install -r requirements.txt

#RUN python3 manage.py migrate


EXPOSE 8000

CMD uwsgi \
    --http 0.0.0.0:8000 \
    --thunder-lock \
    --single-interpreter \
    --enable-threads \
    --processes=2 \
    --wsgi-file frontpageapp/wsgi.py
