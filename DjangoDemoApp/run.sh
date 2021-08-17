#!/bin/bash

export NEW_RELIC_CONFIG_FILE=newrelic.ini
newrelic-admin run-program gunicorn config.wsgi:application -t 120
