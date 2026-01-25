from pages.login_page import LoginPage
import time
def test_login(browser):
    
    login_page = LoginPage(browser)
    login_page.open("/bank/login")
    
    login_page.login(username="testuser", password= "password")
    login_page.wait_for_exact_url("https://demoqa.ru/bank")
    assert browser.current_url == "https://demoqa.ru/bank"
