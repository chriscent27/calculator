FROM python:3.8.5
MAINTAINER chriscent27@gmail.com

COPY . /calculator
WORKDIR /calculator

CMD python calculator.py
