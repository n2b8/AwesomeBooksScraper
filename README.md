# AwesomeBooksScraper

## Description
AwesomeBooksScraper is a sophisticated tool for scraping book information from AwesomeBooks.com, including title, ISBN, condition, author, price, and category. This scraper uses ScrapeOps.io's Fake Headers API and loads data into a remote MongoDB. It's designed to obey the site's robots.txt file and is built using the Scrapy Python framework.

## Installation
To deploy this scraper, cloning this repository onto the machine that will run the scraper is recommended. There are various open-source, free, and paid monitoring systems that can be used. Important: In the `settings.py` file, update your own MongoDB connection information and ScrapeOps API key. This implementation uses environment variables for these configurations.

## Usage
To start scraping, use the command: `scrapy crawl awesomebooks`.

## Features
- Extracts key details like title, ISBN, condition, author, price, and category.
- Adheres to robots.txt file for ethical scraping.
- Currently, it does not include proxy switching capabilities but this may be added in the future.

## Acknowledgments
- Special thanks to ScrapeOps.io's Python Scrapy Playbook, a valuable resource for beginners available at [ScrapeOps Python Scrapy Playbook](https://scrapeops.io/python-scrapy-playbook/).
- Scrapy Framework: For more information on Scrapy, visit [Scrapy.org](https://scrapy.org).

## Personal Learning Journey
This project has been instrumental in my learning journey with the Scrapy framework and data mining, enhancing my skills in web scraping and data analysis.
