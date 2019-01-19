# The application Dockerfile
#
# Copyright (c) 2019, Alexandre Hamelin <alexandre.hamelin gmail.com>
#
FROM python:3-alpine AS builder
LABEL maintainer="Alexandre Hamelin <alexandre.hamelin gmail.com>" \
      copyright="Copyright (c) 2019, Alexandre Hamelin <alexandre.hamelin gmail.com>" \
      license="MIT"

# Update pip and build the requirements as wheel files.
RUN pip install -qU pip
RUN apk update -q
RUN apk add -q openssl-dev libffi-dev build-base

COPY . /app
WORKDIR /app
# Improvement: don't bake the wheels directory into the image
RUN [ -d wheels ] || pip wheel -qw wheels -r requirements.txt && rm -f pip-selfcheck.json

#----------------------------------------------------------------------------
FROM python:3-alpine
LABEL maintainer="Alexandre Hamelin <alexandre.hamelin gmail.com>" \
      copyright="Copyright (c) 2019, Alexandre Hamelin <alexandre.hamelin gmail.com>" \
      license="MIT"
# Update pip in the container and grab the app from the builder container.
# No need for virtualenv, which will cause otherwise some problems when the app
# is mounted from the host for development (permissions, especially if running
# in user namespace, etc.).
RUN pip install -qU pip
COPY --from=builder /app /app
WORKDIR /app
RUN pip install -q wheels/*.whl
RUN adduser -D app && chown -R app:app /app
USER app
ARG FLASK_APP
ARG FLASK_ENV
ENV FLASK_ENV=${FLASK_ENV:-development}
ENV FLASK_APP=${FLASK_APP:-changeme}
EXPOSE 5000
CMD exec flask run -h ::
