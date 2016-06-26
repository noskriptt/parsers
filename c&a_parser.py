#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from parser import Parser
from db_translator import YandexTranslate
import threading

# Site
SITE = "http://www.c-and-a.com/de/de/shop/index.html"

PRODUCT_ITEM = ['.detailsTabContent detailsTabContentDetail1',
                '.detailsTabContent detailsTabContentDetail2', 'div.productImages']
MENU_ITEMS = ('div#mainNavHeaderInner', 'href')
SUBMENU_ITEMS = ['div#navileft', 'ul.level1', 'span']


def main():
    our_site = Parser(SITE)
