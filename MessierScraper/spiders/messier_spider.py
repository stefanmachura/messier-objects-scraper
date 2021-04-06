from scrapy import Spider, Request
from MessierScraper.item_loaders import MessierLoader
from MessierScraper.items import MessierscraperItem


class MessierSpider(Spider):
    name = "MessierSpider"

    def start_requests(self):
        urls = ["http://www.messier.seds.org/m/mindex.html"]
        for url in urls:
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        objects = response.xpath("//pre/a")
        # print(objects)
        yield from response.follow_all(objects, self.parse_object)

    def parse_object(self, response):
        m = MessierLoader(item=MessierscraperItem(), response=response)

        m.add_xpath("name", "//center/h1/text()")
        m.add_xpath("right_ascension", "//table/tr[1]/td[1]/text()")
        m.add_xpath("declination", "//table/tr[2]/td[1]/text()")
        m.add_xpath("distance", "//table/tr[3]/td[1]/text()")
        m.add_xpath("brightness", "//table/tr[4]/td[1]/text()")
        m.add_xpath("dimensions", "//table/tr[5]/td[1]/text()")

        return m.load_item()
