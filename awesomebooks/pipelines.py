# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo


class AwesomebooksPipeline:
    def process_item(self, item, spider):
        return item

# Basic pipeline template, can be expanded for custom processing
class AwesomebooksPipeline:
    def process_item(self, item, spider):
        # Processes each item passed from the spider
        return item

# Pipeline for processing and cleaning up the price data
class PricePipeline:
    def process_item(self, item, spider):
        # Remove the pound sign from the price and convert it to float
        if item['price_gbp'].startswith('£'):
            item['price_gbp'] = item['price_gbp'][1:] # Strip the pound sign
        item['price_gbp'] = float(item['price_gbp']) # Convert string to float
        return item

# Pipeline for storing items in a MongoDB database
class MongoPipeline:
    def open_spider(self, spider):
        # Establish connection to MongoDB when the spider opens
        self.client = pymongo.MongoClient(spider.settings.get('MONGO_URI'))
        self.db = self.client[spider.settings.get('MONGO_DATABASE')]

    def close_spider(self, spider):
        # Close the MongoDB connection when the spider closes
        self.client.close()

    def process_item(self, item, spider):
        # Insert the item into the MongoDB database
        self.db.all.insert_one(dict(item))  # 'all' is the collection name
        return item