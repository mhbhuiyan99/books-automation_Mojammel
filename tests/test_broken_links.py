from pages.home_page import HomePage
import requests

def test_broken_links(page):

    home = HomePage(page)
    home.open()

    links = page.locator("a")

    hrefs = set()

    for i in range(links.count()):
        href = links.nth(i).get_attribute("href")

        if href:
            hrefs.add(page.url.rsplit("/", 1)[0] + "/" + href if not href.startswith("http") else href)

    session = requests.Session()
    session.trust_env = False

    for url in hrefs:
        response = session.get(url)
        assert response.status_code == 200