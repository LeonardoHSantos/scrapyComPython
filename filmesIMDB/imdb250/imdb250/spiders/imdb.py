import scrapy


class ImdbSpider(scrapy.Spider):
    name = 'imdb'
    # pagina específica do site "mais populares"
    start_urls = ['https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm']

    def parse(self, response):  # função para retorno das requisições feitas no site
        # loop para retornar valores na tag selecionada
        for filmes in response.css('.titleColumn'):
            yield{  # função geradora (retorna mais do que um valor, pode ser utilizada para uma série de valores ao invez de usar o return )
                # retorna o nome do filme
                'titulo': filmes.css('.titleColumn a::text').get(),
                # retorna o ano do filme
                'ano': filmes.css('.secondaryInfo::text').get()[1: -1],
                # retorna a nota de avaliação do filme
                'nota': response.css('Strong::text').get()
            }
