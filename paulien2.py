from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
import re
class PoemsSpider(CrawlSpider):
    name = "poems"

    allowed_domains = ['www.poets.org']
    start_urls = ['https://www.poets.org/poetsorg/poems']
    rules = (
        Rule(LinkExtractor(allow= '/poem',canonicalize=True, unique=True),  
             callback="parse_item",follow=True),
    )
    def parse_item(self, response):
        if re.match('.*/poetsorg/poem/.*',response.url) is not None: 
            poem = response.xpath('//*[@id="poem-content"]').get()
            filename=response.url.split("/")[-1] + '.html'
            try:
                with open(filename, "w") as f:
                    f.write(response.url+'\n'+poem)   
            except:
                with open(filename, "w", encoding="utf-8") as f:
                    f.write(response.url+'\n'+poem)
            print("all good")
        else:
            print(response.url)
            
        
            
    
