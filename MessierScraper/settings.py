BOT_NAME = "MessierScraper"

SPIDER_MODULES = ["MessierScraper.spiders"]
NEWSPIDER_MODULE = "MessierScraper.spiders"


ROBOTSTXT_OBEY = True


ITEM_PIPELINES = {
    "MessierScraper.pipelines.FieldsCleanupPipeline": 300,
    "MessierScraper.pipelines.DimensionsNormalizationPipeline": 500,
    "MessierScraper.pipelines.JSONConverterPipeline": 700,
}

FEED_EXPORTERS = {
    "csv": "scrapy.exporters.CsvItemExporter",
}
FEED_FORMAT = "csv"
FEED_URI = "objects.csv"
