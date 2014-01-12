import os
from fabric.api import *

"""
In order to deploy, run "fab <env> deploy"
"""

# Config. Adjust these settings according to your server
# If you need to specify a file system path, please add a trailing slash
config = {
    'stage': {
        'server': 'you@server',
        'project_root': '~/sites/here-i-am-stage/',  # The absolute path to the project
        'source_root': 'src',  # A relative path to folder containing the manage.py file
        'virtualenv': {
            'workon_name': 'here-i-am-stage',
        },
        'git': {
            'server_name': 'origin',
            'branch_name': 'stage',
        },
        'webserver': {
            'touch_file': 'wsgi/default_site.wsgi'  # A relative path to folder containing the manage.py file
        }
    },
}


# Environments. Add as much as you defined in "config"
def stage():
    env.environment = 'stage'
    env.hosts = [config[env.environment]['server']]


def live():
    env.environment = 'live'
    env.hosts = [config[env.environment]['server']]


# Fab Tasks
def deploy():
    """
    Deploy, migrate, collect static files, restart webserver
    """
    global ABSOLUTE_SOURCE_ROOT
    ABSOLUTE_SOURCE_ROOT = os.path.join(config[env.environment]['project_root'], config[env.environment]['source_root'])

    global ABSOLUTE_TOUCH_FILE
    ABSOLUTE_TOUCH_FILE = os.path.join(config[env.environment]['project_root'], config[env.environment]['webserver']['touch_file'])

    global ABSOLUTE_MANAGE_FILE
    ABSOLUTE_MANAGE_FILE = os.path.join(ABSOLUTE_SOURCE_ROOT, 'manage.py')

    _git_pull()
    _migrate()
    _collect_static_files()
    _restart_webserver()


# Helpers
ABSOLUTE_SOURCE_ROOT = ''
ABSOLUTE_TOUCH_FILE = ''
ABSOLUTE_MANAGE_FILE = ''


def __activate():
    return '. /etc/bash_completion.d/virtualenvwrapper && workon {0} '.format(
        config[env.environment]['virtualenv']['workon_name'],
    )


def __deactivate():
    return 'deactivate'


def _git_pull():
    with cd(ABSOLUTE_SOURCE_ROOT):
        run('git pull {0} {1}'.format(
            config[env.environment]['git']['server_name'],
            config[env.environment]['git']['branch_name'])
        )


def _migrate():
    with cd(ABSOLUTE_SOURCE_ROOT):
        run(
            __activate() +\
            '&& python {0} migrate && '.format(ABSOLUTE_MANAGE_FILE) +\
            __deactivate()
        )


def _syncdb():
    with cd(ABSOLUTE_SOURCE_ROOT):
        run(
            __activate() +\
            '&& python {0} syncdb && '.format(ABSOLUTE_MANAGE_FILE) +\
            __deactivate()
        )


def _collect_static_files():
    with cd(ABSOLUTE_SOURCE_ROOT):
        run(
            __activate() +\
            '&& python {0} collectstatic --noinput && '.format(ABSOLUTE_MANAGE_FILE) +\
            __deactivate()
        )


def _restart_webserver():
    run('touch {0}'.format(ABSOLUTE_TOUCH_FILE))
