#!/bin/bash
# Displays the body of a GET request
if [ $(curl -w "\n%{http_code}" "$1" -Ls | tail -1) -eq "200" ]; then
	curl -L -X GET "$1"
fi
