# -*- coding: utf-8 -*-
import scrapy


class JdSpider(scrapy.Spider):
    name = "jd"
    allowed_domains = ["www.jd.com"]
    start_urls = (
        'http://www.jd.com/1057746.html',
    )

    def parse(self, response):
        pass
