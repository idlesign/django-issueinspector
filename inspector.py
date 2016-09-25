#! /usr/bin/env python3
import os

from django.conf.urls import url

from issueinspector.views import inspector_main


RUNNER_NAME = 'inspector'
DEBUG = True
SECRET_KEY = 'fake'
ROOT_URLCONF = RUNNER_NAME


INSTALLED_APPS = [
    'issueinspector',
    'xross',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.template.context_processors.request',
            ],
        },
    },
]


urlpatterns = [
    url(r'^$', inspector_main, name='index'),
]


if __name__ == '__main__':
    import webbrowser
    from time import sleep

    from django.core.management import call_command
    from django.core.wsgi import get_wsgi_application

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', RUNNER_NAME)

    application = get_wsgi_application()

    address = '127.0.0.1:8000'

    webbrowser.open('http://%s' % address)
    call_command('runserver', address)
