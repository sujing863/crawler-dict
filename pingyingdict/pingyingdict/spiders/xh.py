# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class XhSpider(CrawlSpider):
    name = 'xh'
    allowed_domains = ['xh.5156edu.com']
    start_urls = ['http://xh.5156edu.com/pinyi.html']

    rules = (
        # Rule(LinkExtractor(allow='s\/blog.*\.html', restrict_xpaths='//span[@class="atc_title"]'),
        #              callback='parse_item'),
        # Rule(LinkExtractor(restrict_xpaths='//div[@class="SG_page"]//a[contains(.,"下一页")]'))，
        # html2 / c01.html          //a[@class="fontbox"]
        Rule(LinkExtractor(allow='http://xh.5156edu.com/'+'html2.*\.html',restrict_xpaths='//td'), callback='parse_item', follow=True),
        # /html3/5381.html
        Rule(LinkExtractor(allow='http://xh.5156edu.com/'+'html3.*\.html',restrict_xpaths='//td'),callback='parse_item1', follow=True),
    )

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item

    def parse_item1(self, response):
        item = {}
        item['letter'] = response.xpath('//td[@class="font_22"]/text()').extract_first().replace("\r", "")\
            .replace("\n", "")
        item['more'] = ''.join(response.xpath('//td[@class="font_18"]//text()').extract()).strip()\
            .replace("\r", "").replace("\n", "")
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item