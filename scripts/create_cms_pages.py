#!/usr/bin/env python
from configurations import importer
importer.install()

from cms.api import create_page

home = create_page('Home', 'home.html', 'en', slug='home', in_navigation=True, published=True)
about_us = create_page('About Us', 'subsite.html', 'en', slug='about-us', in_navigation=True, published=True)
dropdown = create_page('Dropdown', 'subsite.html', 'en', slug='dropdown', in_navigation=True, published=True)
sub_1 = create_page('Sub 1', 'subsite.html', 'en', slug='sub-1', in_navigation=True, published=True, parent=dropdown)
sub_1_1 = create_page('Sub 1.1', 'subsite.html', 'en', slug='sub-1-1', in_navigation=True, published=True, parent=sub_1)
sub_2 = create_page('Sub 2', 'subsite.html', 'en', slug='sub-2', in_navigation=True, published=True, parent=dropdown)