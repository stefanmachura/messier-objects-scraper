# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MessierscraperPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        brightness = adapter.get("brightness")
        brightness = brightness.strip()
        brightness = brightness.replace("(mag)", "")
        adapter["brightness"] = brightness

        name = adapter.get("name")
        name = name.strip()
        adapter["name"] = name

        distance = adapter.get("distance")
        distance = distance.rstrip()
        distance = distance.replace("(kly)", "")
        try:
            distance = float(distance)
        except:
            distance = None
        else:
            distance *= 1000
        adapter["distance"] = distance

        dimensions = adapter.get("dimensions")
        dimensions = dimensions.rstrip()
        dimensions = dimensions.replace(" (arc min)", "")
        adapter["dimensions"] = dimensions

        return item


class DimensionsNormalizationPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        dimensions = adapter.get("dimensions")
        if "x" in dimensions:
            x, y = dimensions.split("x")
            adapter["dim_x"] = x
            adapter["dim_y"] = y
        else:
            adapter["dim_x"] = dimensions
            adapter["dim_y"] = dimensions
        return item
