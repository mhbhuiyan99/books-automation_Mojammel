def test_homepage(page):
    page.goto("https://books.toscrape.com/index.html")

    print("Current URL: ",page.url)
    print("Page Title: ", page.title())
    assert page.url == "https://books.toscrape.com/index.html"
    assert page.title() == "All products | Books to Scrape - Sandbox"

    headings =  page.locator("h1, h2, h3, h4, h5, h6")
    print(headings)
    print(headings.count())

    for i in range(headings.count()):
        heading = headings.nth(i)
        assert heading.is_visible()

        text = heading.text_content() or ""
        assert text.strip() != ""

        print(text)

