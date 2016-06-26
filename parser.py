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
        """
        Function: category_menu_parse
        Summary: Get level 1 menu
        Examples: Parser.category_menu_parse()
        Attributes: 
            @param (items): list tags css
        Returns: dict('category':'link')
        """
        catalog_menu = {}

        return catalog_menu

    def subcategory_menu_parse(self,  items):
        ''' Out format dict ('category' : 'link') '''
        subcategory_menu = {}

        return subcategory_menu

    def producs_in_categories(self):
        pass

    def product(self):
        pass

    def product_name(self):
        pass

    def product_price(self):
        """ Получаем цену на товар """
        pass

    def product_details(self):
        """ Получаем данные о характеристиках товара, если они есть"""
        pass

    def produc_materials(self):
        """ Получаем данные о материалах продукта, если они есть"""
        pass


def _to_csv(nFile, *data):
    """
    Import to csv file:	nFile - name file for write data; *data - list or tuple.
    Name | Category | SubCategory | Price | Tech Details | Images links | 

        """
    pass
