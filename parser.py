#!/usr/bin/env python3
# -*- encoding:utf-8 -*-

from urllib.parse import urljoin
from urllib.request import urlopen

from lxml.html import fromstring
import csv


class Parser(object):

    """ Universal class for parsing site """

    def __init__(self, url, *args, **kwargs):
        ''' Open site as HTML code '''
        super(Parser, self).__init__()
        self.siteUrl = url
        self.siteHTML = fromstring(urlopen(self.siteUrl).read())

    def category_menu_parse(self, items):
        ''' Out format dict ('category' : 'link') '''
        catalog_menu = {}

        return catalog_menu

    def subcategory_menu_parse(self,  items):
        ''' Out format dict ('category' : 'link') '''
        subcategory_menu = {}

        return subcategory_menu

    def producs_in_categories(self):
        pass

    def product_name(self, *items):
        """ Parse product with price, images and configuration """
        product_NAs = []

        return product_NAs

    def product_price(self):
        pass

    def product_details(self):
        pass


def _to_csv(nFile, *data):
    """
    Import to csv file:	nFile - name file for write data; *data - list or tuple.
    Name | Category | SubCategory | Price | Tech Details | Images links | 

        """
    pass
