from pages.home_page import HomePage

def test_homepage(page):

    home = HomePage(page)
    home.open()

    assert page.url == HomePage.URL
    assert page.title() == "All products | Books to Scrape - Sandbox"

    headings = page.locator("h1,h2,h3,h4,h5,h6")

    assert headings.count() > 0

    for i in range(headings.count()):

        heading = headings.nth(i)
        assert heading.is_visible()

        text = heading.text_content() or ""
        assert text.strip() != ""

    assert home.get_books_count() > 0