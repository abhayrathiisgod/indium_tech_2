FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir /CODE
WORKDIR /CODE
COPY . /CODE/
RUN pip install -r requirements.txt




