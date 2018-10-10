# Dockerfile for the app
#
# Copyright (c) 2017, Alexandre Hamelin <alexandre.hamelin gmail.com>
#
FROM python:3.4-alpine
LABEL maintainer="Alexandre Hamelin <alexandre.hamelin gmail.com>" \
      copyright="Copyright (c) 2017, Alexandre Hamelin <alexandre.hamelin gmail.com>" \
      license="MIT"

RUN pip install virtualenv
COPY . /app
WORKDIR /app
RUN virtualenv /app
RUN . bin/activate && \
    apk --no-cache add git libffi-dev build-base && \
    pip install -r requirements.txt && \
    rm -fr pip-selfcheck.json ~/.cache && \
    apk del git libffi-dev build-base
RUN sed -i -e 's/\.iteritems/.items/g' lib/*/site-packages/flaskext/genshi.py
ENV FLASK_DEBUG=${FLASK_DEBUG:-}
EXPOSE 5000
CMD . bin/activate && exec flask run -h ::
