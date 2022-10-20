#!/bin/bash
#get statue code from http header  work just task(curl -sI "$1" | grep "HTTP/" |  cut -d " " -f 2)
curl -s -o /dev/null --write-out "%{http_code}"
