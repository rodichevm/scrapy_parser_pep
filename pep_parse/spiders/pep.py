import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import PEP_DOMAIN


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = [PEP_DOMAIN]
    start_urls = [*(f'https://{domain}/' for domain in allowed_domains)]

    def parse(self, response):
        for pep_link in response.css('a[href^="pep-"]'):
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        number, name = response.css('.page-title::text').get().split(' – ')
        yield PepParseItem(
            number=number[4:],
            name=name,
            status=response.css('abbr::text').get()
        )
