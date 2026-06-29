import requests

def test_broken_links(page):

    page.goto("https://books.toscrape.com/index.html")

    links = page.locator("a")

    hrefs = set()

    for i in range(links.count()):
        href = links.nth(i).get_attribute("href")

        if href:
            hrefs.add(page.url.rsplit("/", 1)[0] + "/" + href if not href.startswith("http") else href)

    for url in hrefs:
        response = requests.get(url)

        assert response.status_code == 200, f"{url} returned {response.status_code}"