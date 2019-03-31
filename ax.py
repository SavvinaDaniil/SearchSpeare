from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
import re

class PoemsSpider(CrawlSpider):
    name = "poems"

    allowed_domains = ['famouspoetsandpoems.com']
    start_urls = ['http://famouspoetsandpoems.com/poets.html']
    rules = (
        Rule(LinkExtractor(allow= '/poets/'),  callback="parse_item",follow=True),
    )
    def parse_item(self, response):
        if re.match('.*/poets/.*/poems/.*',response.url) is not None: 
            head=response.xpath("/html/head/title/text()").get()
            title = str(head).split(' - Poem by ')[0]
            author = str(head).split(' - Poem by ')[-1]

            poem = "\n".join(response.xpath("*//div[5]/text()").extract())
            filename=response.url.split("/")[-3]+"-"+response.url.split("/")[-1] + '.html'
            try:
                with open(filename, "w") as f:
                    f.write(response.url+'\n'+title+'\n'+author+'\n'+poem)   
            except:
                with open(filename, "w", encoding="utf-8") as f:
                    f.write(response.url+'\n'+title+'\n'+author+'\n'+poem)   
            print("all good")
        else:
            print("its:"+response.url)
        
            