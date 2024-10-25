#!/bin/bash

rm db.sqlite3
rm -rf ./petapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations petapi
python3 manage.py migrate petapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens

