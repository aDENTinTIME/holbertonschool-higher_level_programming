#!/bin/bash
# Displays 'You got me!'
curl 0.0.0.0:5000/catch_me -LsX PUT -d "user_id=98"
