#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from datetime import datetime

AUTHOR = 'Alexander Alemayhu'
SITENAME = 'building in the\ntwenty-first century'
SITEDESC = 'A blog about software development, technology, and creative insights in the twenty-first century.'
SITEURL = ''

# Plugin configuration
PLUGIN_PATHS = ['plugins']
PLUGINS = ['contribution_graph']

PATH = 'content'
TIMEZONE = 'Europe/Oslo'
DEFAULT_LANG = 'en'

# Theme settings
THEME = 'themes/build21'
CURRENTYEAR = datetime.now().year

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('GitHub', 'https://github.com/'),)

# Social widget
SOCIAL = (('GitHub', 'https://github.com/alemayhu'),)

DEFAULT_PAGINATION = 10

# Use document-relative URLs
RELATIVE_URLS = True
