#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 

@author: Professor Wergeles 
"""

import scrapy

class BrickSetSpider(scrapy.Spider):
    name = "brickset_spider"
    start_urls = ['https://brickset.com/sets/year-2019']

    def parse(self, response):
        SET_SELECTOR = ".set"

        for brickset in response.css(SET_SELECTOR):

            NAME_SELECTOR = "h1 ::text"

            yield {
                'name': brickset.css(NAME_SELECTOR).extract_first(),
            }