FROM python:3.7-slim

LABEL homepage="https://haydencardwell.com"
LABEL maintainer="Hayden Cardwell <admin@cardwell.cloud>"

WORKDIR /ds-docker

ADD https://automation.deepsecurity.trendmicro.com/sdk/20_0/v1/dsm-py-sdk.zip /ds-docker/sdk-temp/

RUN apt update && apt install -y unzip
RUN unzip /ds-docker/sdk-temp/dsm-py-sdk.zip -d /ds-docker/sdk-temp
RUN pip install /ds-docker/sdk-temp/ && rm -rf /ds-docker/sdk-temp/*

COPY ./app ./app

CMD [ "python", "./app/main.py" ]
