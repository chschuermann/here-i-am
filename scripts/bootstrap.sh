#!/usr/bin/env bash

# Install the required packages
pip install -r requirements/environments/development.txt

# Copy the directory holding the environment variables
cp -R ./envs_example/ ./envs

# Copy the example settings module
cp src/website/settings_example.py src/website/settings.py

# Add the source folder to the Python path
add2virtualenv $VIRTUAL_ENV ./src/

# Populate the database
python ./src/manage.py syncdb --all --noinput
python ./src/manage.py migrate --fake
python ./src/manage.py createsuperuser

envdir ./envs/ python ./scripts/create_cms_pages.py
