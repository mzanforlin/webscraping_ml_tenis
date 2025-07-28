import scrapy


class MercadolivreSpider(scrapy.Spider):
    name = "mercadolivre"
    allowed_domains = ["lista.mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/tenis-corrida-masculino"]

    def parse(self, response):
        products = response.css('div.poly-card__content')
        
        for product in products:

            yield  {'brand' : products.css('span.poly-component__brand::text').get()
            }    

    pass
