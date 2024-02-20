import scrapy

from pep_parse.constants import PEP_URL
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    start_urls = [PEP_URL]

    def parse(self, response):
        for pep_link in response.css('a[href^="pep-"]'):
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        pep_name = response.css('.page-title::text').get().split()
        yield PepParseItem(
            {'number': int(pep_name[1]),
             'name': ' '.join(pep_name[3:]),
             'status': response.css('abbr::text').get()}
        )
