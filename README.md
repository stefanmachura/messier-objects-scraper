### Messier Objects List Crawl Spider

This is a Scrapy spider to crawl the Messier Object List website (http://www.messier.seds.org/m/mindex.html)

The result is a csv file with MO data that can be later used for other projects.

How to use it:

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
scrapy crawl MessierSpider

```

#astronomy #astrophotography #messierobjects
