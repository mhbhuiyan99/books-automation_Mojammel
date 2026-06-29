from pages.home_page import HomePage

def test_product_image(page):
    home = HomePage(page)
    home.open()

    max_pages = 5
    current = 0

    while current < max_pages:
        images = page.locator("article.product_pod img")
        assert images.count() > 0

        for i in range(images.count()):
            image = images.nth(i)

            assert image.is_visible()

            src = image.get_attribute("src")
            alt = image.get_attribute("alt")
            cls = image.get_attribute("class")

            assert src
            assert alt
            assert "thumbnail" in cls

        next_button = page.locator("li.next a")

        if next_button.count() == 0:
            break

        next_button.click()
        current += 1