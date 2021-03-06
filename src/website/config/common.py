# -*- coding: utf-8 -*-
from configurations import Configuration, values
from django.core.urlresolvers import reverse_lazy
from os.path import abspath, dirname, join, normpath

ugettext = lambda s: s


class BaseSettings(Configuration):
    # Absolute filesystem path to the "website" folder. Example: /path/to/project-folder/src/website/
    WEBSITE_ROOT = dirname(dirname(abspath(__file__)))

    # Absolute filesystem path to the "src" folder. Example: /path/to/project-folder/src/
    SOURCE_ROOT = dirname(WEBSITE_ROOT)

    # Absolute filesystem path to the top-level project folder. Example: /path/to/project-folder/
    PROJECT_ROOT = dirname(SOURCE_ROOT)

    DEBUG = values.BooleanValue(False)
    TEMPLATE_DEBUG = values.BooleanValue(False)

    DEFAULT_FROM_EMAIL = values.EmailValue('webmaster@example.com')
    SERVER_EMAIL = values.EmailValue(DEFAULT_FROM_EMAIL)

    ADMINS = (
        (u'Webmaster', u'c.schuermann@gmail.com'),
    )

    MANAGERS = ADMINS

    # Hosts/domain names that are valid for this site; required if DEBUG is False
    # See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
    ALLOWED_HOSTS = values.ListValue()

    # Whether to prepend the "www." subdomain to URLs that don't have it.
    PREPEND_WWW = values.BooleanValue(False)

    # Local time zone for this installation. Choices can be found here:
    # http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
    # although not all choices may be available on all operating systems.
    # In a Windows environment this must be set to your system time zone.
    TIME_ZONE = 'Europe/Zurich'

    # Language code for this installation. All choices can be found here:
    # http://www.i18nguy.com/unicode/language-identifiers.html
    LANGUAGE_CODE = 'en'

    LANGUAGES = (
        ('de', ugettext(u'German')),
        ('en', ugettext(u'English')),
    )

    SITE_ID = 1

    # If you set this to False, Django will make some optimizations so as not
    # to load the internationalization machinery.
    USE_I18N = True

    # If you set this to False, Django will not format dates, numbers and
    # calendars according to the current locale.
    USE_L10N = True

    # If you set this to False, Django will not use timezone-aware datetimes.
    USE_TZ = True

    # Absolute filesystem path to the directory that will hold user-uploaded files.
    # Example: "/var/www/example.com/media/"
    MEDIA_ROOT = normpath(join(PROJECT_ROOT, 'media'))

    # URL that handles the media served from MEDIA_ROOT. Make sure to use a
    # trailing slash.
    # Examples: "http://example.com/media/", "http://media.example.com/"
    MEDIA_URL = '/media/'

    # Absolute path to the directory static files should be collected to.
    # Don't put anything in this directory yourself; store your static files
    # in apps' "static/" subdirectories and in STATICFILES_DIRS.
    # Example: "/var/www/example.com/static/"
    STATIC_ROOT = normpath(join(PROJECT_ROOT, 'static'))

    # URL prefix for static files.
    # Example: "http://example.com/static/", "http://static.example.com/"
    STATIC_URL = '/static/'

    # Additional locations of static files
    STATICFILES_DIRS = (
        # Put strings here, like "/home/html/static" or "C:/www/django/static".
        # Always use forward slashes, even on Windows.
        # Don't forget to use absolute paths, not relative paths.
        normpath(join(WEBSITE_ROOT, 'static')),
    )

    # List of finder classes that know how to find static files in
    # various locations.
    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
        # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
    )

    # Don't put the secret key here. Read the docs for more information.
    SECRET_KEY = values.SecretValue()

    # List of callables that know how to import templates from various sources.
    TEMPLATE_LOADERS = (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
        # 'django.template.loaders.eggs.Loader',
    )

    TEMPLATE_CONTEXT_PROCESSORS = (
        'django.contrib.auth.context_processors.auth',
        'django.core.context_processors.debug',
        'django.core.context_processors.i18n',
        'django.core.context_processors.media',
        'django.core.context_processors.static',
        'django.core.context_processors.tz',
        'django.core.context_processors.request',
        'django.contrib.messages.context_processors.messages',
        'cms.context_processors.media',
        'sekizai.context_processors.sekizai',
    )

    MIDDLEWARE_CLASSES = (
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.locale.LocaleMiddleware',
        'django.middleware.doc.XViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'cms.middleware.page.CurrentPageMiddleware',
        'cms.middleware.user.CurrentUserMiddleware',
        'cms.middleware.toolbar.ToolbarMiddleware',
        'cms.middleware.language.LanguageCookieMiddleware',
    )

    ROOT_URLCONF = 'website.urls'

    # Python dotted path to the WSGI application used by Django's runserver.
    WSGI_APPLICATION = 'website.wsgi.application'

    # List of locations of the template source files.
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Note that these paths should use Unix-style forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    TEMPLATE_DIRS = (
        normpath(join(WEBSITE_ROOT, 'templates', 'sites', 'default')),
        normpath(join(WEBSITE_ROOT, 'templates', 'sites')),
        normpath(join(WEBSITE_ROOT, 'templates')),
    )

    INSTALLED_APPS = (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'djangocms_admin_style',
        'django.contrib.admin',
        'django_extensions',
        'south',
        'filer',
        'easy_thumbnails',
        'ganalytics',
        'south',
        'floppyforms',
        'djangocms_text_ckeditor',
        'cms',
        'cms.stacks',
        'mptt',
        'menus',
        'sekizai',
        'reversion',
        'cms.plugins.flash',
        'cms.plugins.googlemap',
        # 'cms.plugins.text',  # Replaced by djangocms_text_ckeditor
        # 'cms.plugins.snippet',  # Not recommended to use
        # 'cms.plugins.file',  # Replaced by cmsplugin_filer_video
        # 'cms.plugins.twitter',  # Not working anymore due to the Twitter API changes
        # 'cms.plugins.link',  # Replaced by cmsplugin_filer_video
        # 'cms.plugins.picture',  # Replaced by cmsplugin_filer_video
        # 'cms.plugins.teaser',  # Replaced by cmsplugin_filer_video
        # 'cms.plugins.video',  # Replaced by cmsplugin_filer_video
        'cmsplugin_filer_file',
        'cmsplugin_filer_folder',
        'cmsplugin_filer_image',
        'cmsplugin_filer_teaser',
        'cmsplugin_filer_video',
        'cmsplugin_filer_link',
    )

    # A sample logging configuration. The only tangible logging
    # performed by this configuration is to send an email to
    # the site admins on every HTTP 500 error when DEBUG=False.
    # See http://docs.djangoproject.com/en/dev/topics/logging for
    # more details on how to customize your logging configuration.
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'simple': {
                'format': '%(levelname)s %(message)s'
            },
            'verbose': {
                'format': '[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s',
            },
        },
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse'
            },
            'require_debug_true': {
                '()': 'django.utils.log.RequireDebugTrue'
            }
        },
        'handlers': {
            'mail_admins': {
                'level': 'ERROR',
                'filters': ['require_debug_false'],
                'class': 'django.utils.log.AdminEmailHandler'
            },
            'console': {
                'level': 'DEBUG',
                'filters': ['require_debug_true'],
                'class': 'logging.StreamHandler',
                'formatter': 'verbose'
            },
        },
        'loggers': {
            'django.request': {
                'handlers': ['mail_admins'],
                'level': 'ERROR',
                'propagate': True,
            },
        }
    }

    # Use the bcrypt hasher
    PASSWORD_HASHERS = (
        'django.contrib.auth.hashers.BCryptPasswordHasher',
        'django.contrib.auth.hashers.PBKDF2PasswordHasher',
        'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
        'django.contrib.auth.hashers.SHA1PasswordHasher',
        'django.contrib.auth.hashers.MD5PasswordHasher',
        'django.contrib.auth.hashers.CryptPasswordHasher',
    )

    CMS_TEMPLATES = (
        ('home.html', 'Home'),
        ('subsite.html', 'Subsite'),
        ('styleguide.html', 'Styleguide'),
    )

    CMS_LANGUAGES = {
        1: [
            {
                'code': 'de',
                'name': ugettext(u'German'),
                'public': True,
            },
            {
                'code': 'fr',
                'name': ugettext(u'French'),
                'public': True,
            },
            {
                'code': 'en',
                'name': ugettext(u'English'),
                'public': True,
            },
            {
                'code': 'it',
                'name': ugettext(u'Italian'),
                'public': False,
                'redirect_on_fallback': True,
            },
        ],
        'default': {
            'public': False,
            'redirect_on_fallback': False,
            'hide_untranslated': True,
        }
    }

    THUMBNAIL_PROCESSORS = (
        'easy_thumbnails.processors.colorspace',
        'easy_thumbnails.processors.autocrop',
        #'easy_thumbnails.processors.scale_and_crop',
        'filer.thumbnail_processors.scale_and_crop_with_subject_location',
        'easy_thumbnails.processors.filters',
    )

    GANALYTICS_TRACKING_CODE = values.Value('', environ_prefix='')

    THUMBNAIL_QUALITY = 95
