#!/bin/bash
# displays the body of the response.
curl -sX POST "$1" -H 'Content-Type: application/json' -d "@$2" 
