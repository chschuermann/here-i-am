#!/bin/bash

# This is an example script for running management commands in a crontab.
#
# Usage:
# * SSH into your server.
# * Make a copy of this file and adjust as needed.
# * Launch "crontab -e" and add the script:
#
# # Project-Name: Short description
# 0  12   *   *   *   /path/to/this_script.sh > /dev/null 2>&1
#
# Important:
# - Make sure to add the "src" folder on the Python path in the virtual env (add2virtualenv).
# - Ensure that the file has the execute bit set.

source ~/path/to/virtualenv/bin/activate
cd ~/path/to/src-folder/
python manage.py management_command
deactivate
