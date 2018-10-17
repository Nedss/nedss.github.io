#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Nedss'
SITENAME = "Nedss en Vrac !"
SITEURL = 'https://nedss.github.io/index.html'
THEME = 'pelican-themes/pure-single'
PATH = 'content'

STATIC_PATHS = ['assets', 'images']

TAGLINE = "Mes passions en vrac : Culture japonaise, jeux-vidéos et bien d'autres !"
COVER_IMG_URL = "/assets/img/banner.jpeg"
PROFILE_IMG_URL = "/assets/img/nedss_wankul.png"


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
SOCIAL = (('twitter', 'http://www.twitter.com/Nedss_'),
          ('github', 'http://www.github.com/nedss'),)

MENUITEMS = (
    ('Accueil', '/index.html'),
    ('Historique', '/archives.html'),
    ('Categories', '/categories.html'),)

CATEGORY_URL = 'category/{slug}.html'
CATEGORY_SAVE_AS = 'category/{slug}.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

DEFAULT_PAGINATION = 10
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
DELETE_OUTPUT_DIRECTORY = True


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
