#!/usr/bin/env bash

docker build -t event-planner-api . && docker-compose up -d
