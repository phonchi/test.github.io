#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://phonchi.github.io'
SITELOGO = SITEURL + SITELOGO
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TAG_FEED_ATOM = 'feeds/tag_%s.atom.xml'
FEED_MAX_ITEMS = 100

DELETE_OUTPUT_DIRECTORY = False

# Following items are often useful when publishing

DISQUS_SITENAME = "phonchi"
#GOOGLE_ANALYTICS = ""
