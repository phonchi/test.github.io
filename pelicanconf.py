#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from pathlib import Path
import re


AUTHOR = 'phonchi'
SITENAME = "phonchi's blog"
SITEURL = ''

PATH = 'content'
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}/index.html'
ARTICLE_LANG_URL = 'posts/{date:%Y}/{date:%m}/{slug}/{lang}.html'
ARTICLE_LANG_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}/{lang}.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
PAGE_LANG_URL = '{slug}/{lang}.html'
PAGE_LANG_SAVE_AS = '{slug}/{lang}.html'

TIMEZONE = 'Asia/Taipei'

DEFAULT_LANG = 'zh-Hant'
DEFAULT_DATE = 'fs'
DEFAULT_DATE_FORMAT = '%b %d, %Y'
USE_FOLDER_AS_CATEGORY = False
TYPOGRIFY = True
MD_EXTENSIONS = [
    'codehilite(css_class=highlight)',
    'smarty',
    'toc',
    'extra',
]

# Static path
STATIC_PATHS = ['pics']

# Find blog post dirs based on regular expression
ARTICLE_PATHS = []
_CONTENT_DIR = Path('content')
_BLOG_ROOT = _CONTENT_DIR / 'blogs'
blog_dirs_by_month = []
for dir_pth in _BLOG_ROOT.iterdir():
    if dir_pth.is_dir() and re.match(r'^\d{4}-\d{2}$', dir_pth.stem):
        blog_dirs_by_month.append(
            dir_pth.relative_to(_CONTENT_DIR).as_posix()
        )
STATIC_PATHS += blog_dirs_by_month
ARTICLE_PATHS += blog_dirs_by_month

# Plugin
PLUGIN_PATHS = ['./pelican-plugins', ]
PLUGINS = ['render_math']

# Theme
THEME = "./theme-flex"


def sort_by_len(value, len_key=-1, reversed=False):
    return sorted(
        value,
        key=lambda t: (-len(t[len_key]), t),
        reverse=reversed,
    )
JINJA_FILTERS = {
    'sort_by_len': sort_by_len  # required by theme-flex
}

# Flex Theme setting
SITETITLE = "phonchi's Blog"
SITESUBTITLE = "Code / Stat / Bioinfo"
SITEDESCRIPTION = SITETITLE
SITELOGO = "/pics/STAR_logo.PNG"
MAIN_MENU = True
MENUITEMS = [
    ('Archives', '/archives.html'),
    ('Categories', '/categories.html'),
    ('Tags', '/tags.html'),
]
COPYRIGHT_YEAR = 2015
CC_LICENSE = {
    'name': 'Creative Commons Attribution',
    'version': '4.0',
    'slug': 'by'
}
OG_LOCALE = 'zh_TW'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
    ('facebook', 'https://www.facebook.com/twSecure/?fref=ts'),
    ('github', 'https://github.com/phonchi'),
)

SUMMARY_MAX_LENGTH = 24
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
