# -*- coding: utf-8 -*-
import scrapy
from TheTimeNews.items import ThetimenewsItem
import re


class StocksSpider(scrapy.Spider):
    name = "stocks"
    start_urls = ['http://www.nybooks.com/daily/page/1/']


    def parse(self, response):
        info =  response.css('.blog_post')
        info_title = info.css('h2')
        info_urls = info_title.css('a[href*=http]::attr(href)').extract()
        for url in info_urls:
            yield scrapy.Request(url, callback=self.parse_news)
        for i in range(2,179):
            page_url = 'http://www.nybooks.com/daily/page/{}/'.format(i)
            yield scrapy.Request(page_url, callback=self.parse)


    def parse_news(self, response):
        news = ThetimenewsItem()
        article = response.css('.blog_post')
        article_head = article.css('h2::text').extract()[0].strip()
        article_author = article.css('.author')
        article_author = article_author.css('a::text').extract()[0].strip()
        article_body = article.css('p::text').extract()
        article_all = ''
        for part in article_body:
        	article_all += "".join(part.strip())

        article_all.replace('\xa0','')
        article_all.replace('\t','').replace('\n','')

        article_time = article.css('time::text').extract()[0]
        article_data = re.findall('[A-Z].*', article_time)[0]
        news['news_head'] = article_head
        news['news_data'] = article_data
        news['news_author'] = article_author
        news['news_body'] = article_all
        news['news_link'] = response.url

        yield news



