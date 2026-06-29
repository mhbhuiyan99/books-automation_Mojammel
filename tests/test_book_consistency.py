from pages.home_page import HomePage

def test_book_data_consistency(page):

    home = HomePage(page)
    home.open()

    indices = home.random_book_indices()

    for index in indices:
        homepage_title = home.get_book_title(index)
        homepage_price = home.get_book_price(index)

        home.open_book(index)

        detail_title = home.get_detail_title()
        detail_price = home.get_detail_price()

        assert homepage_title == detail_title
        assert homepage_price == detail_price

        home.go_back()