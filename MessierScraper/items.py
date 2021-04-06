from dataclasses import dataclass
import scrapy


class MessierscraperItem(scrapy.Item):
    name = scrapy.Field()
    right_ascension = scrapy.Field()
    declination = scrapy.Field()
    distance = scrapy.Field()
    brightness = scrapy.Field()
    dimensions = scrapy.Field()
    dim_x = scrapy.Field()
    dim_y = scrapy.Field()
