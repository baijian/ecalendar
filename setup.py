# -*- coding: utf-8 -*-

from setuptools import find_packages
from setuptools import setup

setup (
    name = "ecalendar",
    version = "1.0.dev",

    package_dir = {"": "src"},
    packages = find_packages("src"),

#    entry_points = {
#        "console_scripts": [
#            "manage = ecanlendar.manage:main"
#        ]
#    },

    install_requires = [
        "tendo==0.2.2",
        "django-csvimport==0.9",
        "lxml==3.2.1",
        "meld3==0.6.10",
        "supervisor==3.0b2",
        "uWSGI==1.9.12",
         #"wsgiref==0.1.2"
        "Django==1.5.1",
        "MySQL-python==1.2.4",
        "chardet==2.1.1",
    ],

    author = "Ecalendar Team.",
    description = "Ecalendar",
    url = "http://huodongrili.com/"
)

