# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class IpinfoPipeline(object):
    def process_item(self, item, spider):
        item['name'] = item['name'].strip()
        item['asn'] = item['asn'].strip()
        item['ip'] = item['ip'].strip()
        return item
