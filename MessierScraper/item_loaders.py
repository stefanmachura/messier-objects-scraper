from itemloaders.processors import TakeFirst
from scrapy.loader import ItemLoader


class MessierLoader(ItemLoader):

    default_output_processor = TakeFirst()
