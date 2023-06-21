#!/usr/bin/env bash
# exit on error
set -o errexit
pip install --upgrade pip
pip install -r requirements.txt
#pip install poetry

#poetry lock --no-update
#poetry install

python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate
python init_base.py
