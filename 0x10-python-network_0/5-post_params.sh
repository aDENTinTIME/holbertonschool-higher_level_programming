#!/bin/bash
# Creates POST request with variables
curl -sX POST -d "email=hr@holbertonschool.com" -d "subject=I will always be here for PLD" "$1"
