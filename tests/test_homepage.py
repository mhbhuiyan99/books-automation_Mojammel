def test_homepage(page):
    page.goto("https://books.toscrape.com/index.html")

    print("Current URL: ",page.url)
    print("Page Title: ", page.title())
    assert page.url == "https://books.toscrape.com/index.html"
    assert page.title() == "All products | Books to Scrape - Sandbox"