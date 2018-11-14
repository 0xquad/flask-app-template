# Dockerfile for the app
#
# Copyright (c) 2018, Alexandre Hamelin <alexandre.hamelin gmail.com>
#
FROM python:3-alpine
LABEL maintainer="Alexandre Hamelin <alexandre.hamelin gmail.com>" \
      copyright="Copyright (c) 2018, Alexandre Hamelin <alexandre.hamelin gmail.com>" \
      license="MIT"

ARG FLASK_ENV=development
ARG FLASK_APP

# The project needs to be initialized with ./init.sh first.
RUN pip install -qU pip && pip install -q virtualenv
COPY . /app
WORKDIR /app
RUN virtualenv /app
RUN . bin/activate && \
    apk --no-cache add git libffi-dev build-base && \
    pip install -qr requirements.txt && \
    rm -fr pip-selfcheck.json ~/.cache && \
    apk del git libffi-dev build-base
ENV FLASK_ENV=${FLASK_ENV:-development}
ENV FLASK_APP=${FLASK_APP:-changeme}
EXPOSE 5000
CMD ./run.sh
