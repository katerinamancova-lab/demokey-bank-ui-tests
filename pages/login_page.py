
from pages.base_page import BasePage

from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    
    LOGIN_BTN = (By.CSS_SELECTOR, "#root > div > div.min-h-screen.bg-slate-50.flex.flex-col.justify-center.py-12.sm\:px-6.lg\:px-8 > div.mt-8.sm\:mx-auto.sm\:w-full.max-w-5xl > div > div:nth-child(1) > div > form > div.flex.items-center.p-6.pt-0 > button")
    # (By.XPATH, "//button[@type='submit']") это локатор если одна кнопка
    
    
    def login(self, username, password):
        self.fill(self.USERNAME, username)
        self.fill(self.PASSWORD, password)
        
        self.click(self.LOGIN_BTN)