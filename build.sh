#!/usr/bin/env bash
# exit on error
set -o errexit
pip install --upgrade pip
pip install poetry

poetry lock --no-update
poetry install

poetry run python manage.py collectstatic --no-input
poetry run python manage.py migrate
poetry run python python init_base.py