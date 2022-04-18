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
class TestBlock(unittest.TestCase):
    def test_get_page_id(self):
        pass
    def test_get_page_child(self):
        pass
    def test_update_page_title(self):
        pass
    def test_add_child(self):
        pass

if __name__ == "__main__":
    unittest.main()