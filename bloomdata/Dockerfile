FROM ubuntu:18.04

ENV PYTHONBUFFER=1

RUN apt update
RUN apt upgrade -y
RUN apt install python3 python3-pip curl -y
RUN pip3 install pandas numpy
RUN apk add nano

