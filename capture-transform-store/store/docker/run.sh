#!/bin/bash

mkdir pgadmin-vol && mkdir database-vol

sudo chown -R 5050:5050 pgadmin-vol

docker-compose up

