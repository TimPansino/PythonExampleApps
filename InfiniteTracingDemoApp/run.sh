#!/bin/bash

export NEW_RELIC_CONFIG_FILE=newrelic.ini
source ./.env  # Add license key
newrelic-admin run-program gunicorn main:app -t 120
