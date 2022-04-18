#!/usr/bin/env python
# encoding: utf-8

'''
Python Standard Libraries
'''
from datetime import datetime
import unittest
import os
import sys
import uuid

'''
Libraries
'''
from dotenv import load_dotenv, find_dotenv

'''
Local Modules
'''
sys.path.insert(0, os.path.abspath('.'))
from notion.client import *
from notion.utils import *

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
class TestUtils(unittest.TestCase):
    def test_now(self):
        date = now()
        assert isinstance(date, int)
        assert date > 0
    def test_extract_id(self):
        id = extract_id(PAGE_URL)
        assert id == str(uuid.UUID('5751cd88a7694420910464fa378e9a96'))
        id2 = extract_id('5751cd88a7694420910464fa378e9a96')
        assert id == id2
        block_id = extract_id('https://www.notion.so/whitecaprsc/NotionPY-SDK-5751cd88a7694420910464fa378e9a96#b02acafc512f414983b5bdba940146be')
        assert block_id == str(uuid.UUID('b02acafc512f414983b5bdba940146be'))
        database_page_id = extract_id('https://www.notion.so/whitecaprsc/Hello-World-0c587c40f9794d4a887887596a9b1ab3')
        assert database_page_id == str(uuid.UUID('0c587c40f9794d4a887887596a9b1ab3'))
    def test_extract_id_from_url(self):
        pass
    def test_extract_id_from_url_invalid(self):
        self.assertRaises(InvalidNotionIdentifier, extract_id, "https://www.notion.so/whitecaprsc/")
        self.assertRaises(InvalidNotionIdentifier, extract_id, "https://www.notion.so/whitecaprsc/123")
        self.assertRaises(InvalidNotionIdentifier, extract_id, "https://www.notion.so/whitecaprsc/123-abc-456-123")
        self.assertRaises(InvalidNotionIdentifier, extract_id, "https://www.notion.so/whitecaprsc/123-abc-456-123?v=123")
        self.assertRaises(InvalidNotionIdentifier, extract_id, "https://www.notion.so/whitecaprsc/123-abc-456-123?v=123#abc") 
    def test_get_embed_data(self):
        # data = get_embed_data(remove_signed_prefix_as_needed("https://s3.us-west-2.amazonaws.com/secure.notion-static.com/a22afe1c-d7fa-48a2-acc2-26470d6c8c16/1990_nissan_skyline_gt-r_1554825990abd8bafd95ad44797dIMG_4171.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220413%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220413T012551Z&X-Amz-Expires=86400&X-Amz-Signature=cf5603c01c8cfb59dfeac97a1220ee46bf0003d98002ec2656a33e136c4a929c&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%221990_nissan_skyline_gt-r_1554825990abd8bafd95ad44797dIMG_4171.jpg%22&x-id=GetObject"))
        # print(data)
        # assert "error_code" not in data.keys()
        # assert "provider_url" in data.keys()
        pass
    def test_get_embed_data_invalid(self):
        data = get_embed_data("https://s3.us-west-2.amazonaws.com/secure.notion-static.com/a22afe1c-d7fa-48a2-acc2-26470d6c8c16/1990_nissan_skyline_gt-r_1554825990abd8bafd95ad44797dIMG_4171.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220413%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220413T012551Z&X-Amz-Expires=86400&X-Amz-Signature=cf5603c01c8cfb59dfeac97a1220ee46bf0003d98002ec2656a33e136c4a929c&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%221990_nissan_skyline_gt-r_1554825990abd8bafd95ad44797dIMG_4171.jpg%22&x-id=GetObject")
        assert data['error_code'] == 404
        pass
    def test_get_embed_link(self):
        data = get_embed_link(remove_signed_prefix_as_needed("https://s3.us-west-2.amazonaws.com/secure.notion-static.com/a22afe1c-d7fa-48a2-acc2-26470d6c8c16/1990_nissan_skyline_gt-r_1554825990abd8bafd95ad44797dIMG_4171.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220413%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220413T012551Z&X-Amz-Expires=86400&X-Amz-Signature=cf5603c01c8cfb59dfeac97a1220ee46bf0003d98002ec2656a33e136c4a929c&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%221990_nissan_skyline_gt-r_1554825990abd8bafd95ad44797dIMG_4171.jpg%22&x-id=GetObject"))
        assert data != None
    def test_get_embed_link_invalid(self):
        pass
    def test_slugify(self):
        pass
    def test_slugify_invalid(self):
        pass
    def test_get_by_path(self):
        pass
    def test_get_by_path_invalid(self):
        pass

if __name__ == "__main__":
    unittest.main()