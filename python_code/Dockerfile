FROM ubuntu:16.04

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

RUN mkdir /automation

WORKDIR /automation

COPY ./requirements.txt /automation

RUN pip install -r requirements.txt

COPY . /automation

CMD python app.py && tail -F /var/log/apt/history.log
