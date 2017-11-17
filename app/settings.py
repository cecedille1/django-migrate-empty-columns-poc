# -*- coding: utf-8 -*-

import os.path
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = '4'

INSTALLED_APPS = [
    'app',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'database.sqlite3'),
    }
}
