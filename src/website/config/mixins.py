# -*- coding: utf-8 -*-
import os
from configurations import values


class DevMixin(object):
    DEBUG = values.BooleanValue(True)
    TEMPLATE_DEBUG = values.BooleanValue(True)

    @property
    def DATABASES(self):
        SQLITE_ROOT = os.path.join(super(DevMixin, self).PROJECT_ROOT, 'database')
        try:
            os.makedirs(SQLITE_ROOT)
        except OSError:
            pass

        return {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(SQLITE_ROOT, 'dev.sqlite3'),
            }
        }

    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


class ProdMixin(object):
    DEBUG = values.BooleanValue(False)
    TEMPLATE_DEBUG = values.BooleanValue(False)
    DATABASES = values.DatabaseURLValue()


class MobileSiteMixin(object):
    SITE_ID = 2

    @property
    def TEMPLATE_DIRS(self):
        return (
            os.path.normpath(os.path.join(super(MobileSiteMixin, self).WEBSITE_ROOT, 'templates', 'sites', 'mobile')),
        ) + super(MobileSiteMixin, self).TEMPLATE_DIRS