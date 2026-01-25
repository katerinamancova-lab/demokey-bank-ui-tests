from pages.base_page import BasePage

from selenium.webdriver.common.by import By

class RegistrPage(BasePage):
    
    NAME = (By.ID, "firstName")
    LASTNAME = (By.ID, "lastName")
    EMAIL = (By.ID,"email")
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    CONFIRMPASSWORD = (By.ID, "confirmPassword")
    
    REGISTR_BTN = (By.CSS_SELECTOR, "#root > div > div.min-h-screen.bg-slate-50.flex.flex-col.justify-center.py-12.sm\:px-6.lg\:px-8 > div.mt-8.sm\:mx-auto.sm\:w-full.sm\:max-w-md > div > form > div.flex.items-center.p-6.pt-0 > button")
  
    # (By.XPATH, "//button[@type='submit']") это локатор если одна кнопка
    
    
    def registr(self, firstName, lastname, email, username, password, confirmPassword ):
        self.fill(self.NAME, firstName)
        self.fill(self.LASTNAME, lastname)
        self.fill(self.EMAIL, email)
        self.fill(self.USERNAME, username)
        self.fill(self.PASSWORD, password)
        self.fill(self.CONFIRMPASSWORD, confirmPassword)
        
        self.click(self.REGISTR_BTN)