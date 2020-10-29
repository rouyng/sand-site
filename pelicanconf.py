#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'SAND AZ'
SITENAME = 'SAND'
TAGLINE = 'PHOENIX — ARIZONA — USA'
SITEURL = 'http://www.sand.zone'

THEME = 'themes/martin-sand'

PATH = 'content'
STATIC_PATHS = ['img']

TIMEZONE = 'America/Phoenix'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

#SLICKNAV Menu
MENUITEMS = (('SAND', '../index.html'),
		 	('EVENTS', '../category/events.html'),
         	('SUPPORT', '../pages/support.html'),
         	('ABOUT', '../pages/about.html'),
         )


# Social widget
SOCIAL = (('instagram', 'http://instagram.com/sand.zone'),)

DEFAULT_PAGINATION = False
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
GOOGLE_ANALYTICS = 'UA-129773634-1'
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
