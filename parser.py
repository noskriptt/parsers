#!/usr/bin/env python3
# -*- encoding:utf-8 -*-

from urllib.parse import urljoin
from urllib.request import urlopen
import threading
from lxml.html import fromstring
import csv


class Parser(object):

    """ Universal class for parsing site """

    def __init__(self, url, *args, **kwargs):
        ''' Open site as HTML code '''
        super(Parser, self).__init__()
        self.url = url

    def __get_html(self, url):
        self.siteUrl = url
        self.siteHTML = fromstring(urlopen(self.siteUrl).read())
        return self.siteHTML

    def __get_element(self, element, item):
        return element.cssselect(item)

    def __get_name(self, obj, css_item):
        return obj.get(css_item)

    def __get_href(self, obj, css_item):
        return obj.get(css_item)

    def category_menu_parse(self, items):
        catalog_menu = {}
        last = list(items)[-2:]
        items = (items[:-2])
        if len(items) > 1:
            html = self.__get_html(self.url)
            for el in items:
                menu = self.__get_element(html, el)

        elif len(items) == 1:
            html = self.__get_html(self.url)
            menu = self.__get_element(html, items[0])
            for el in menu[0]:
                try:
                    name = self.__get_name(el, last[0])
                    href = self.__get_href(el, last[1])
                    catalog_menu[name] = href
                except ValueError as e:
                    continue
        else:
            pass
        return catalog_menu

    def subcategory_menu_parse(self, items, url=None):
        subcategory_menu = {}
        last = list(items)[-2:]
        items = (items[:-2])
        if len(items) > 1:
            html = self.__get_html(url)
            for elem in items:
                menu = self.__get_element(html, elem)
            print(menu)
        elif len(items) == 1:
            html = self.__get_html(url)
            menu = self.__get_element(html, items[0])
            for el in menu[0]:
                try:
                    name = self.__get_name(el, last[0])
                    href = self.__get_href(el, last[1])
                    subcategory_menu[name] = href
                except ValueError as e:
                    raise e
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


class Product(object):
    """docstring for Product"""

    def __init__(self, url):
        super(Product, self).__init__()
        self.url = url

    def details(self):
        pass

    def price(self):
        pass

    def materials(self):
        pass


def _to_csv(nFile, *data):
    """
    Import to csv file:	nFile - name file for write data; *data - list or tuple.
    Name | Category | SubCategory | Price | Tech Details | Images links |

        """
    pass
