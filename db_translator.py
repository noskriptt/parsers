#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

# Translate using API v1.5 translate.yandex.ru
# Using your API-key from https://tech.yandex.ru/translate/

# api-key for me '******'

import sys
import json

import requests
from lxml import etree

import abc


class Translator(metaclass=abc.ABCMeta):

    def __init__(self):
        self._from_xml = None

    @abc.abstractproperty
    def _response(self):
        return

    def __str__(self):
        return self.get_result()

    def get_result(self):
        return self.__parse_json() if self._from_xml is False else self.__parse_xml

    def ret_text(self, path='translated'):
        return self.__read_json(path) if self._from_xml is False else self.__read_xml(path)

    def __parse_xml(self):
        root = etree.fromstring(self._response)
        return '; '.join([i.text for i in root])

    def __parse_json(self):
        return '; '.join(self._response['text'])

    def __read_xml(self, path):
        try:
            return self._response
        except IOError:
            return None

    def __read_json(self, path):
        try:
            return json.dumps(self._response)
        except IOError:
            return False


class YandexTranslate(Translator):
    """ SOME EXAMPLES:
    python3 translator.py robot en-uk
    python3 translator.py 'Люблю грозу в начале мая' en
        FOR IN FUNCTION EXAMPLES:
    t_text = YandexTranslate(t_text, 'en-ru')
    print(t_text.get_result())
"""

    API_KEY = 'trnsl.1.1.20160625T030211Z.c261dcc9030989fc.b9ca91a5604815701109019bd73f3f85a461c422'
    LINK_JSON = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    LINK_XML = 'https://translate.yandex.net/api/v1.5/tr/translate'

    def __init__(self, text, lang, fmt='plain', from_xml=False):
        super(YandexTranslate, self).__init__()
        self.data = {
            'key': self.API_KEY,
            'text': text,
            'lang': lang,
            'format': fmt,
        }
        self._from_xml = from_xml

    @property
    def _response(self):
        if self._from_xml is True:
            return requests.post(self.LINK_XML, params=self.data).context
        else:
            return requests.post(self.LINK_JSON, params=self.data).json()


def translate_de_ru(func):
    def wrapper(words):
        de_input = YandexTranslate(words, 'en')
        ru_output = YandexTranslate(de_input, 'en-ru')
        return ru_output
    return wrapper
