from pages.base_page import BasePage

from selenium.webdriver.common.by import By

class TransferPage(BasePage):
    
    SEND_BY_NAME = (By.CSS_SELECTOR, '[data-testid="transfer-recipient-input"]')
    AMOUNT = (By.CSS_SELECTOR, '[data-testid="transfer-amount-input"]')
    BALANCE = (By.CSS_SELECTOR, '[data-testid="available-balance"]')
    SUCCESS_MESSAGE = (By.XPATH, "//*[contains(., 'Успеш') or contains(., 'отправ') or contains(., 'Перевод') or contains(., 'выполн')]")

   
    TRANSFER_BTN = (By.XPATH, "//button[@type='submit']")
    
    TAB_BY_ACCOUNT = (By.XPATH, "//button[contains(normalize-space(.), 'По сч')]")
    TAB_BY_RECIPIENT = (By.XPATH, "//button[contains(., 'По получателю') or contains(., 'По имени')]")
    ERROR_MESSAGE = (By.XPATH, "//*[contains(., 'Ошибка') or contains(., 'Невер') or contains(., 'невер') or contains(., 'недостат') or contains(., 'OTP') or contains(., 'код')]")

    # (By.XPATH, "//button[@type='submit']") это локатор если одна кнопка
    
    
    def transfer(self, recipient: str, amount: str):
        self.fill(self.SEND_BY_NAME, recipient)
        self.fill(self.AMOUNT, amount)
       
        self.click(self.TRANSFER_BTN)
    
    def open_account_tab(self):
        self.click(self.TAB_BY_ACCOUNT)
        # ждём, что активная вкладка = "По счёту"
        self.wait_visible((By.XPATH, "//button[@data-state='active' or @aria-selected='true'][normalize-space()='По счёту']"))    
    def transfer_by_account(self, account_number: str, amount: str):
        self.click(self.TAB_BY_ACCOUNT)
        
        self.fill(self.SEND_BY_NAME, account_number)
        self.fill(self.AMOUNT, amount)
        self.click(self.TRANSFER_BTN)
   