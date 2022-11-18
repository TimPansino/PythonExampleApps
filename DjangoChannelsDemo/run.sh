#!/bin/bash

APP="channelsdemo.asgi:application"
export NEW_RELIC_CONFIG_FILE=newrelic.ini

newrelic-admin run-program daphne $APP
# newrelic-admin run-program gunicorn $APP -k uvicorn.workers.UvicornWorker
# newrelic-admin run-program uvicorn $APP