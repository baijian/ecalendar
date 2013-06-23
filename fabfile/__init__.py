# -*- coding: utf-8 -*-

from fabric.api import *
from fabric.contrib.files import sed, contains
from fabtools import deb, user, require, files

from .vagrant import vagrant

@task
def develop():
    import os
    proxy = os.environ.get("http_proxy")
    if proxy:
        with shell_env(http_proxy=proxy):
            _develop()
    else:
        _develop()

def _develop():
    """
    Provision the environment for ecalendar
    """
    if not contains('/etc/default/locale', 'en_US.UTF-8'):
        sed('/etc/default/locale', 'en_US', 'en_US.UTF-8', use_sudo=True, shell=True)

    # sources.list
    if not contains('/etc/apt/sources.list', 'mirrors.163'):
        sed('/etc/apt/sources.list', 'us\.archive\.ubuntu', 'mirrors.163', use_sudo=True, shell=True)
        deb.update_index(quiet=False)

    require.mysql.server(password='123456')
    
    # build-essential
    require.deb.packages([
        'libxml2-dev',
        'libxslt1-dev',
        'build-essential',
        'python-dev',
        'cmake',
        'libmysqlclient-dev',
        'libssl-dev'
    ])

    require.deb.packages([
        'python-distribute',
        'python-pip'
    ])

    with cd ('/vagrant'):
        sudo('easy_install -U distribute')
        sudo('python setup.py develop', shell=True)
    
