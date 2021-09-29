import scrapy


class ImdbSpider(scrapy.Spider):
    name = 'imdb'
    start_urls = ['https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm']

    def parse(self, response):
        for filmes in response.css('.titleColumn'):
            yield{
                'titulo': filmes.css('.titleColumn a::text').get(),
                'ano': filmes.css('.secondaryInfo::text').get()[1: -1],
                'nota': response.css('Strong::text').get()
            }
