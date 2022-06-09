import scrapy
from bs4 import BeautifulSoup
from wiki_tarea.items import articles, article

class ArticleSpider(scrapy.Spider):
    name = 'article'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Wikipedia:Featured_articles']

    def parse(self, response):

        host = self.allowed_domains[0]
        counter = 0

        print('STARTING SPIDER CRAWLING')
       
        for link in response.css('.featured_article_metadata > a'):
            # CANTIDAD DE ARTICULOS A REVISAR
            if counter >= 3:
                break
          
            link =  f"https://{host}{link.attrib.get('href')}"
            yield response.follow(link,callback=self.parse_detail, meta={'URL' : link})#,'title':title})

            # COUNTER TO LIMIT QUANTITY OF CRAWLS
            counter = counter + 1

    def parse_detail(self,response):

        items = articles()
        item = article()

        soup = BeautifulSoup(response.text, 'lxml')

        items["link"] = response.meta['URL']
       
        # titulo con response.css
        #item["title"] = response.css('.firstHeading::text').extract()
        # titulo con Beautifulsoup
        item["title"] = soup.h1.string

        item["paragraph"] = list()
        
        # Parrafo con BeautifulSoup
        item["paragraph"].append(soup.get_text().replace('\n', '').replace('^', ''))

        # Parrafo con repsonse.css 
        #for text in response.css('.mw-parser-output > p::text').get():
        #    soup = BeautifulSoup(text,features="lxml").text()
        #    item["paragraph"].append(soup.get_text())
            #item["paragraph"].append(text)

        items["body"] = item

        return items