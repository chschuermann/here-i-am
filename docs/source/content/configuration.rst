*************
Configuration
*************

The following Django settings variables may be set through environment variables (the name of the
environment variable is in parenthesis):

**ALLOWED_HOSTS** (DJANGO_ALLOWED_HOSTS)

Example: .example.com,.example.com.

**DEBUG** (DJANGO_DEBUG)

**TEMPLATE_DEBUG** (DJANGO_TEMPLATE_DEBUG)

**SECRET_KEY** (DJANGO_SECRET_KEY)

**DEFAULT_FROM_EMAIL** (DJANGO_DEFAULT_FROM_EMAIL)

**SERVER_EMAIL** (DJANGO_SERVER_EMAIL)

**PREPEND_WWW** (DJANGO_PREPEND_WWW)

**DATABASES** (DATABASE_URL)

Example: postgres://username:password@localhost/db_name

.. note:: This only works for the production configuration.

If you need to specify multiple database, you may override it in the ``settings.py``. You might
want to store ``connection_string`` for each database in a separate
environment variable and load it accordingly. Example::

     DATABASES = {
        'default': dj_database_url.parse(values.Value(DATABASE_URL_DEFAULT, environ_prefix='')),
        'read_only': dj_database_url.parse(values.Value(DATABASE_URL_READ_ONLY, environ_prefix='')),
     }

Additionally, some project specific settings can be customized through the following environment
variables (the name of the environment variable is in parenthesis):

TODO: Complete according to your project.