#!/usr/bin/env python
# encoding: utf-8

'''
Python Standard Libraries
'''
from datetime import datetime
import unittest
import os
import sys

'''
Libraries
'''
from dotenv import load_dotenv, find_dotenv

'''
Local Modules
'''
sys.path.insert(0, os.path.abspath('.'))
from notion.client import *
from notion.block import *
from notion.collection import NotionDate

'''
Script Environment Set Up
'''
load_dotenv(find_dotenv())

'''
Global variables
'''
API_KEY = os.getenv('API_KEY')
PAGE_URL = os.getenv('PAGE_URL')

'''
Unit Test Classes
'''
class TestStore(unittest.TestCase):
    def test_callback(self):
        pass
    def test_default_store_initialize(self):
        client = NotionClient(api_key=API_KEY)
        assert client._store != None
    def test_store_no_cache_key(self):
        client = NotionClient(api_key=API_KEY)
        assert client._store._cache_key == None
    def test_store_cache_key(self):
        client = NotionClient(api_key=API_KEY, enable_caching=True, cache_key=hashlib.sha256((API_KEY).encode()).hexdigest())
        assert client._store._cache_key == hashlib.sha256((API_KEY).encode()).hexdigest()

if __name__ == "__main__":
    unittest.main()