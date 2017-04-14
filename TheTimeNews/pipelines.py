# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from scrapy import signals
from scrapy.contrib.exporter import XmlItemExporter




class ArticlePipeline(object):
	def process_item(self, item, spider):
		con = pymysql.connect(host="localhost",user="root",password="zxcvbnm",db="papermedia",use_unicode=False, charset="utf8") 
		cur = con.cursor()
		sql = ("insert into the_time_news(head,data,author,body,link)"
			   "values(%s,%s,%s,%s,%s)")
		lis = (item['news_head'], item['news_data'],item['news_author'], item['news_body'], item['news_link'])
		try:
			cur.execute(sql, lis)
			print('adding it!')
		except Exception as e:
			print('Insert error:'+e)
			con.rollback()
		else:
			con.commit()
		cur.close()
		con.close()
		return item
