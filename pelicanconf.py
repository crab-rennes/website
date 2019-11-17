#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHORS = ("Le CRAB",)

SITENAME = "CRAB - Collectif Rennais des Amateurs de Bières"
SITEURL = "http://localhost:8000"

PATH = "content"

TIMEZONE = "Europe/Paris"
DEFAULT_DATE_FORMAT = "%d %B %Y"

DEFAULT_LANG = "fr"

DEFAULT_PAGINATION = False

THEME = "theme"

MENUITEMS = (
    ("Accueil", "/index.html"),
    ("Actus", "/blog.html"),
    (
        "Adhérer",
        "https://www.helloasso.com/associations/collectif-rennais-des-amateurs-de-bieres-crab/adhesions/adhesion-au-crab",
    ),
)
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
DIRECT_TEMPLATES = ["index", "blog"]
STATIC_PATHS = [
    "images",
    "assets",
    "extra/CNAME",
]
EXTRA_PATH_METADATA = {"extra/CNAME": {"path": "CNAME"}}
PLUGIN_PATHS = [
    "plugins",
]

RELATIVE_URLS = True
