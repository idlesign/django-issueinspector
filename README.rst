django-issueinspector
=====================
https://github.com/idlesign/django-issueinspector

.. image:: https://img.shields.io/pypi/v/django-issueinspector.svg
    :target: https://pypi.python.org/pypi/django-issueinspector

.. image:: https://img.shields.io/pypi/dm/django-issueinspector.svg
    :target: https://pypi.python.org/pypi/django-issueinspector

.. image:: https://img.shields.io/pypi/l/django-issueinspector.svg
    :target: https://pypi.python.org/pypi/django-issueinspector


Description
-----------

*Issue inspector for your GitHub repositories*

.. image:: https://img-fotki.yandex.ru/get/27579/153990.b/0_83260_bf5ee282_L.png

This application allows you to inspect issues in your repositories that require your attention.

It could be helpful when you have to manage many repositories, to not to forget what issues you need to attend to.

Wire this application into your existing Django project and you're done.


Requirements
------------

* Python 3.2+
* Django


How to setup
------------

Given your already have your Django project configured do the following simple steps:

1. Add ``issueinspector`` into ``INSTALLED_APPS`` (usually in *settings.py*).
2. Link ``issueinspector.views.inspector_main`` to an URL (usually in *urls.py*)
3. Go to that URL and push ``About`` button for further instructions.
