from selenium.webdriver.common.by import By
from main_page import MainPage
def test_guest_can_go_to_login_page(browser):
    # link = "http://selenium1py.pythonanywhere.com/"
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer "
    page = MainPage(browser, link)
    page.open()

    page.go_to_login_page()
    page.should_be_link()