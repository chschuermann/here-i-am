#################################################################################
Here I Am
#################################################################################

The following quickstart guide will help a contributor to get the project up and running for local development.

Quickstart
==========

You'll have to complete a few simple steps in order to get this project up and running on your development machine:

* Create a virtualenv
* Get the source code
* Install the requirements
* Configure the project in your environment
* Frontend development
* Final steps
* Start coding
* Build the documentation

**Note:** This quickstart guide assumes that you already have *virtualenvwrapper* and *git-flow* installed
on your system.

Create a virtualenv
-------------------

If you're using *virtualenvwrapper* (and you really should be using it if you don't), creating a home for the
project and an associated *virtualenv* is easy as:

.. code:: bash

    mkproject <name-of-the-project>

You can name the project whatever you want because this has no side effects on the project itself or other
contributors. So feel free to substitute ``<name-of-the-project>`` with whatever value that suites your naming
scheme, e.g. <client-project>.

**Working directory**

The command ``mkproject`` automatically changes to the directory of the project. The rest of this quickstart guide
assumes that you are still in this directory because of some relative paths used in some of the commands later in
this guide.

Get the source code
-------------------

Clone the repo to the folder created by the ``mkproject`` command above:

.. code:: bash

    git clone -b master <url-to-the-git-repo> </path/to/the/project/folder>

Then switch to the branch ``develop``. Most of the implementation will be happening in this branch:

.. code:: bash

    git checkout develop

Initialize *git-flow* by running the following command. You can accept all the default values (just keep
hitting <enter>):

.. code:: bash

    git flow init

Install the requirements
------------------------

Now install all the Python packages required by this Django project:

.. code:: bash

    pip install -r requirements/environments/development.txt

Configure the project in your environment
-----------------------------------------

You're now going to configure the environment of your development machine. Make sure that you are still in the
directory of the project, i.e. the directory containing this very README.rst file.

**Python path**

You need to add the ``./src/`` folder to your Python path. If you're using *virtualenvwrapper* this is as easy as
the following command:

.. code:: bash

    add2virtualenv $VIRTUAL_ENV ./src/

**Note:** This command will expand ``./src/`` to its absolute path and print a warning.

**Django settings**

This project uses some third party apps for the configuration of the Django project. This
requires additional configuration of your environment compared to a vanilla Django project setup:

Make a copy of ``./src/website/settings_example.py`` and name it ``settings.py``. You may edit ``settings.py`` as
you please (it won't get added to the repo because of its presence in the gitignore file).

**Environment variables**

Copy the folder ``./envs_example/`` to ``./envs/`` (it won't get added to the repo because of its presence
in the gitignore file).

You may edit the files as you please, but at least you should generate a Django secret key and save it to
``./envs/DJANGO_SECRET_KEY``:

.. code:: bash

    echo -n $(python ./src/manage.py generate_secret_key) > ./envs/DJANGO_SECRET_KEY

**Note:** You no longer have to add ``DJANGO_SETTINGS_MODULE`` to the ``$VIRTUAL_ENV/bin/postactivate``.

**django-admin.py**

In previous projects we showed you how to modify ``django-admin.py`` to meet the new configuration setup.
We don't recommend using ``django-admin.py`` anymore. Please use ``manage.py`` for all future projects.

Frontend development
--------------------

This project uses SASS, Compass and the Zurb Foundation Framework for the frontend development. The Zurb
Foundation Framework is bundled in the ``./src/website/static/sass/foundation`` folder so you don't have to install
the ``zurb-foundation`` gem.

You'll find a Compass config file at ``./src/website/config.rb``. You can use this config file
for the compilation of the *.scss files e.g. with the excellent `CodeKit <http://incident57.com/codekit/>`_ tool.

Final steps
-----------

Change into ``./src/`` directory of the project and populate your database:

.. code:: bash

    python manage.py syncdb --all
    python manage.py migrate --fake

Now launch the development server with the ``runserver`` management command and admire the result in your browser.

Start coding
------------

Now you're all set to contribute to this project. Don't forget to have a look at the documentation for
more information.

Build the documentation (optional)
----------------------------------

This step is optional but very useful if you want to read the project's documentation in a browser.

First you have to change into the directory containing the documentation (``./docs/``) and then you can
build the documentation by running ``make html``.

Once the documentation has been built you may open ``./docs/build/index.html`` in your browser for easier reading.

License
-------

No license available.