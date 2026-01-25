from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import pytest
from loguru import logger
from faker import Faker
from pages.login_page import LoginPage

@pytest.fixture
def auth_user(browser, request):
    # Получаем данные из маркера 'auth_data'
    marker = request.node.get_closest_marker("auth_data")
    if marker:
        login, password = marker.args
    else:
        # Дефолтные значения, если маркер не указан
        login, password = "testuser", "password"
    
    login_page = LoginPage(browser)
    login_page.open("/bank/login")
    login_page.login(login, password)
    return login_page

@pytest.fixture
def browser():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    yield driver
    driver.quit()
@pytest.fixture
def browser():
    options = Options()
    prefs = {
        "credentials_enable_service": False,      # не предлагать сохранять пароли
        "profile.password_manager_enabled": False, # выключить password manager
    }
    options.add_experimental_option("prefs", prefs)

    # 2) отключаем подсказки/попапы/уведомления
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")

    # 3) чтобы Chrome не показывал “Chrome управляется автоматизацией”
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()