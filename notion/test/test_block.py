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
    def test_get_pageblock(self):
        url = PAGE_URL
        client = NotionClient(api_key=API_KEY)
        block = client.get_block(url)
        assert(type(block) == PageBlock)
        assert(block == PageBlock(client, url))
    def test_get_paragraphblock(self):
        url = "https://www.notion.so/whitecaprsc/NotionPY-SDK-5751cd88a7694420910464fa378e9a96#b02acafc512f414983b5bdba940146be"
        client = NotionClient(api_key=API_KEY)
        block = client.get_block(url)
        assert(type(block) == ParagraphBlock)
        assert(block == ParagraphBlock(client, url))
    def test_get_heading1(self):
        url = "https://www.notion.so/whitecaprsc/NotionPY-SDK-5751cd88a7694420910464fa378e9a96#6396f8f6a96c46fd924e38a80a39c774"
        client = NotionClient(api_key=API_KEY)
        block = client.get_block(url)
        assert(type(block) == Heading1Block)
        assert(block == Heading1Block(client, url))
    def test_get_heading2(self):
        url = "https://www.notion.so/whitecaprsc/NotionPY-SDK-5751cd88a7694420910464fa378e9a96#28eec1e2c9804d5fa90c2b53696b2009"
        client = NotionClient(api_key=API_KEY)
        block = client.get_block(url)
        assert(type(block) == Heading2Block)
        assert(block == Heading2Block(client, url))
    def test_get_heading3(self):
        url = "https://www.notion.so/whitecaprsc/NotionPY-SDK-5751cd88a7694420910464fa378e9a96#2234dc1536974d7093c2f125c0240c89"
        client = NotionClient(api_key=API_KEY)
        block = client.get_block(url)
        assert(type(block) == Heading3Block)
        assert(block == Heading3Block(client, url))
    def test_get_collectionvieweblock(self):
        url = "https://www.notion.so/whitecaprsc/ad1e95f5c39e444ba0ce56032fdca90b?v=9ba339fa8a834bb1b7a4238f3f833c81"
        client = NotionClient(api_key=API_KEY)
        block = client.get_block(url)
        assert(type(block) == CollectionViewBlock)
        assert(block == CollectionViewBlock(client, url))
    def test_get_collection_childpage(self):
        url = "https://www.notion.so/whitecaprsc/Hello-World-0c587c40f9794d4a887887596a9b1ab3"
        client = NotionClient(api_key=API_KEY)
        block = client.get_block(url)
        assert(type(block) == ChildPageBlock)
        assert(block == ChildPageBlock(client, url))
    def test_get_inner_childpage(self):
        url = "https://www.notion.so/whitecaprsc/Inner-Page-cd0389af07a444d9aabec5efa9fa3fd4"
        client = NotionClient(api_key=API_KEY)
        block = client.get_block(url)
        assert(type(block) == ChildPageBlock)
        assert(block == ChildPageBlock(client, url))
    def test_get_imageblock(self):
        url = "https://www.notion.so/whitecaprsc/NotionPY-SDK-5751cd88a7694420910464fa378e9a96#e379a5a9eaee49b7923009ffd54b943e"
        client = NotionClient(api_key=API_KEY)
        block = client.get_block(url)
        assert(type(block) == ImageBlock)
        assert(block == ImageBlock(client, url))
    def test_get_columnlist_paragraphblock(self):
        url = "https://www.notion.so/whitecaprsc/NotionPY-SDK-5751cd88a7694420910464fa378e9a96#d2e2d2aba6a24078b50dd66697229f1f"
        client = NotionClient(api_key=API_KEY)
        block = client.get_block(url)
        assert(type(block) == ParagraphBlock)
        assert(block == ParagraphBlock(client, url))
    def test_get_tableblock(self):
        url = "https://www.notion.so/whitecaprsc/NotionPY-SDK-5751cd88a7694420910464fa378e9a96#94ff6866c6a141ef8671c8113dde9c30"
        client = NotionClient(api_key=API_KEY)
        block = client.get_block(url)
        assert(type(block) == TableBlock)
        assert(block == TableBlock(client, url))
    
    

if __name__ == "__main__":
    unittest.main()