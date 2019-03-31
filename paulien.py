from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
import re

class PoemsSpider(CrawlSpider):
    name = "poems"

    allowed_domains = ['www.poetryfoundation.org']
    start_urls = ['https://www.poetryfoundation.org/poems/browse']
    rules = (
        Rule(LinkExtractor(allow= '/poems'),  callback="parse_item",follow=True),
    )
    def parse_item(self, response):
        #the following condition makes sure I only save the actual poems
        if re.match('.*/poems/.*/',response.url) is not None: 
            title = ''.join(response.xpath('//*[@id="mainContent"]/div/div[1]/article/div/div[1]/div/div/div[1]/div/div[1]/h1/text()').get().strip())
            author = response.xpath('//*[@id="mainContent"]/div/div[1]/article/div/div[1]/div/div/div[1]/div/div[2]/div/span/a/text()').get()
            #the poem below is the title the author and the text, I just kept the two first above seperately in case we need them
            poem = response.xpath('//*[@id="mainContent"]/div/div[1]/article/div/div/div/div/div[1]/div').get()
            filename=response.url.split("/")[-1] + '.html'
            #I did the exception handling below cause there were some encoding errors
            try:
                with open(filename, "w") as f:
                    f.write(poem)   
            except:
                with open(filename, "w", encoding="utf-8") as f:
                    f.write(poem)
            
            
        
            
#I could also save the tags of the categories the poem belongs to, what do you think?
