# Import necessary classes from Scrapy framework
from scrapy.spiders import SitemapSpider
from awesomebooks.items import BookItem


# Define the spider class
class AwesomeBooksSpider(SitemapSpider):
    # Spider name used in the command line
    name = "awesomebooks"
    # List of URLs where the sitemap can be found
    sitemap_urls = ['https://www.awesomebooks.com/robots.txt']
    # Rules to extract the URLs (looking for book categories)
    sitemap_rules = [("/books/category/", "parse_category")]

    # Method to parse each category page
    def parse_category(self, response):
        # Select all book items on the page
        books_on_page = response.css('div.item-action.product-item-actions a')

        # Iterate through each book item
        for single_book in books_on_page:
            # Extract book details from data attributes
            book_title = single_book.attrib['data-title']
            book_price = single_book.attrib['data-price']  # Assumes 'sale' price is the actual price
            book_isbn = single_book.attrib['data-isbn']
            book_author = single_book.attrib['data-author']
            book_condition = single_book.attrib['data-condition']
            book_category = single_book.attrib['data-category']

            # Create a BookItem and populate it with extracted data
            book = BookItem()
            book['title'] = book_title
            book['price_gbp'] = book_price
            book['isbn'] = book_isbn
            book['author'] = book_author
            book['condition'] = book_condition
            book['category'] = book_category

            # Yield the book item to the pipeline
            yield book

        # Handling pagination
        # Extract all pagination links
        pagination_links = response.css('a.page-link::attr(href)').getall()

        # Follow each pagination link and reapply this parsing method
        for url in pagination_links:
            yield response.follow(
                url=url,
                callback=self.parse_category
            )
