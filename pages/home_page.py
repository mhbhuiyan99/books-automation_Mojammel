from playwright.sync_api import Page
import random

class HomePage:
    URL = "https://books.toscrape.com/index.html"

    def __init__(self, page):
       self.page = page

    def open(self):
        self.page.goto(self.URL)
    
    def get_books(self):
        return self.page.locator("article.product_pod")
    
    def get_books_count(self):
        books = self.get_books()
        return books.count()

    # ---- Book Information ----

    def get_book_title(self, index):
        book = self.get_books().nth(index)
        return book.locator("h3 a").get_attribute("title")    
    
    def get_book_price(self, index):
        book = self.get_books().nth(index)
        return book.locator(".price_color").text_content()

    def open_book(self, index):
        book = self.get_books().nth(index)
        book.locator("h3 a").click()
    
    # ---- Detail Page ----

    def get_detail_title(self):
        return self.page.locator(".product_main h1").text_content()

    def get_detail_price(self):
        return self.page.locator(".product_main .price_color").text_content()

    def go_back(self):
        self.page.go_back()
    
    # ---- Utilities ----

    def random_book_indices(self, count=5):
        total = self.get_books_count()
        return random.sample(range(total), count)

    