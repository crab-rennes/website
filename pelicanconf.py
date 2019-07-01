#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHORS = (
    u'Le CRAB',
)

SITENAME = u'CRAB - Collectif Rennais des Amateurs de Bières'
SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'Europe/Paris'
DEFAULT_DATE_FORMAT = ('%d %B %Y')

DEFAULT_LANG = u'fr'

DEFAULT_PAGINATION = False

THEME = "theme"

MENUITEMS = (
    (u'Accueil', '/index.html', 'wide'),
    (u'Actus', '/blog.html', 'mobile'),
)
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
DIRECT_TEMPLATES = ['index', 'blog']
STATIC_PATHS = ['images', 'assets', 'extra/CNAME', ]
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}}
PLUGIN_PATHS = ["plugins", ]

RELATIVE_URLS = True
