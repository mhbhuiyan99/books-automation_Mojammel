from pages.home_page import HomePage

def test_random_book_navigation(page):
    
    home = HomePage(page)

    home.open()
    indices = home.random_book_indices()

    for index in indices:
        expected_title = home.get_book_title(index)  # Capture the book title

        home.open_book(index)  # Click the book
        actual_title = home.get_detail_title()
        assert expected_title == actual_title  # H1 title matches selected book title

        home.go_back()  # Navigate back to homepage