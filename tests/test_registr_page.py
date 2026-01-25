from pages.registr_page import RegistrPage
import time
def test_registr(browser):
    
    login_page = RegistrPage(browser)
    login_page.open("/bank/register")
    
    login_page.registr(firstName= "Nik", lastname= "Kin",  email= "test@test.com", username= "HBn",  password= "password", confirmPassword= "password")
    login_page.wait_for_exact_url("https://demoqa.ru/bank/register")
    assert browser.current_url == "https://demoqa.ru/bank/register"