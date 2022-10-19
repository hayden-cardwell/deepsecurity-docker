FROM python:3.7-slim

LABEL homepage="https://haydencardwell.com"
LABEL maintainer="Hayden Cardwell <admin@cardwell.cloud>"

ADD https://automation.deepsecurity.trendmicro.com/sdk/20_0/v1/dsm-py-sdk.zip /home/

RUN apt update && apt install -y unzip
RUN unzip /home/dsm-py-sdk.zip -d /home
RUN pip install /home/ && rm -rf /home/*
