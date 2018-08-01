#!/bin/bash
# Displays the size of the body of the requested URL
curl -s "$1" | wc -c
