import os
from configparser import ConfigParser

from django.shortcuts import render
from xross.toolbox import xross_view, xross_listener

from .utils import fetch_data


CONFIG_NAME = '.inspector.conf'


def inspect(request):
    """Is triggered by AJAX to get actual data from GitHub.

    :param request:
    """
    results = fetch_data(request.POST['username'], request.POST['token'])
    return render(request, 'issueinspector/sub_issues.html', {'repos': results})


@xross_view(inspect)
def inspector_main(request):
    """Main entry point. Link it to URL whatever you like.

    :param request:
    """
    username = ''
    token = ''

    if os.path.exists(CONFIG_NAME):
        conf = ConfigParser()
        conf.read(CONFIG_NAME)
        username = conf['core']['username']
        token = conf['core']['token']

    xross_listener(http_method='POST')
    return render(request, 'issueinspector/index.html', {
        'username': username,
        'token': token,
    })
