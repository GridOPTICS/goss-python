# Use latest slim Python image. Note that it's built on Debian Stretch.
FROM python:3.7-slim

ENV GRIDAPPSD_PORT="61613"
ENV GRIDAPPSD_URI="tcp://localhost:${GOSS_PORT}"
ENV GRIDAPPSD_USER="system"
ENV GRIDAPPSD_PASS="manager"

RUN pip install --upgrade pip

WORKDIR /usr/src/goss-python

COPY requirements.txt ./
##RUN pip3 install -U pip setuptools wheel
##RUN pip3 install ruamel.yaml
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN pip install .
