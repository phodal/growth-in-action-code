#!/usr/bin/env bash
virtualenv --distribute -p /usr/local/bin/python3.5 growth-django
source growth-django/bin/activate
pip install -r requirements.txt
python manage.py test
python manage.py test test