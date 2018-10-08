#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Nedss'
SITENAME = "Nedss' Blog"
SITEURL = ''
THEME = 'pelican-themes/pure-single'
PATH = 'content'

STATIC_PATHS = ['assets']

COVER_IMG_URL = "/Users/nedss/Sites/pelican/vrac_nedss/assets/img/wl_banner.png"
PROFILE_IMG_URL = "assets/img/nedss_wankul.png"


TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

MENUITEMS = (
    ('Historique', 'archives.html'),
    ('Accueil', 'index.html'),
    ('Category', 'categories.html'),)

DEFAULT_PAGINATION = 10
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
