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
class TestClient(unittest.TestCase):
    def test_start_monitoring_argument(self):
        client = NotionClient(api_key=API_KEY, monitor=True, start_monitoring=True)
        assert client._monitor.thread != None
        client.stop_monitoring()
        assert client._monitor.thread == None

    def test_start_monitoring_method(self):
        client = NotionClient(api_key=API_KEY, monitor=True)
        client.start_monitoring()
        assert client._monitor.thread != None
        client.stop_monitoring()
        assert client._monitor.thread == None