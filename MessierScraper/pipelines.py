import csv
import json

from itemadapter import ItemAdapter


class FieldsCleanupPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        brightness = adapter.get("brightness")
        brightness = brightness.strip()
        brightness = brightness.replace("(mag)", "")
        brightness = brightness.replace(" ", "")
        adapter["brightness"] = brightness

        name = adapter.get("name")
        name = name.strip()
        name = name.replace('"', "")
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

        ra = adapter.get("right_ascension")
        ra = ra.rstrip()
        ra = ra.replace(" (h:m)", "")
        ra = ra.replace(" ", "")
        adapter["right_ascension"] = ra

        dec = adapter.get("declination")
        dec = dec.rstrip()
        dec = dec.replace(" (deg:m)", "")
        dec = dec.replace(" ", "")
        adapter["declination"] = dec

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


class JSONConverterPipeline:
    def close_spider(self, spider):
        objects = []
        with open("objects.csv", "r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                    continue
                obj = {}
                for k, v in row.items():
                    obj[k] = v
                objects.append(obj)
        with open("objects.json", "w") as json_file:
            json_file.write(json.dumps(objects, indent=4))
