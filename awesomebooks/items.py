# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AwesomebooksItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class BookItem(scrapy.Item):
    title = scrapy.Field()
    price_gbp = scrapy.Field()
    isbn = scrapy.Field()
    author = scrapy.Field()
    condition = scrapy.Field()
    category = scrapy.Field()
