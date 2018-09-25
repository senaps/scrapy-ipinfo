# -*- coding: utf-8 -*-
import scrapy
from ..items import RangeIP


class IspSpider(scrapy.Spider):
    name = 'isp'
    custom_settings = {'ITEM_PIPELINES':
                           {'ipinfo.pipelines.IpinfoPipeline': 100}
                       }

    allowed_domains = ['ipinfo.io']
    start_urls = ['https://ipinfo.io/countries/ir/']

    def parse(self, response):
        links = response.css('td a::text').extract()
        for link in links:
            url = 'https://ipinfo.io/%s' % link
            yield scrapy.Request(url, callback=self.asn_info)

    def asn_info(self, response):
        row_list = []
        range_rows = response.xpath('/html/body/div/div/section[1]/div/div/div[2]/div/div[4]/div[2]/div/div[1]/table/tbody')
        for row in range_rows.css('tr'):
            asn = response.xpath('/html/body/div/div/section[1]/div/div/div[2]/div/div[1]/div[2]/div/div[1]/div/div[1]/p').css('p ::text').extract_first()
            ip = row.css('td a::text').extract()[0]
            name = row.css('td a::text').extract()[1]
            obj = RangeIP(asn=asn, ip=ip, name=name)
            yield obj



