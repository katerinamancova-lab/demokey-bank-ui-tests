from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from loguru import logger
from selenium.common.exceptions import TimeoutException

class BasePage:
    BASE_URL = "https://demoqa.ru"
    TIMEOUT = 20

    def is_visible(self, locator, timeout=5) -> bool:
        try:
            WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, self.TIMEOUT)

    def open(self, path):
        # чтобы не было https://demoqa.ru//bank/transfer
        url = self.BASE_URL.rstrip("/") + "/" + path.lstrip("/")
        logger.info(f"Open page: {url}")
        self.browser.get(url)

    def click(self, locator):
        """
        Безопасный клик:
        - ждём наличие элемента
        - скроллим к нему
        - пробуем обычный клик
        - если не кликается (оверлей/анимация) → JS click
        """
        logger.info(f"Click: {locator}")

        el = self.wait.until(EC.presence_of_element_located(locator))
        self.browser.execute_script("arguments[0].scrollIntoView({block:'center'});", el)

        try:
            self.wait.until(EC.element_to_be_clickable(locator))
            el.click()
        except Exception:
            self.browser.execute_script("arguments[0].click();", el)

    def fill(self, locator, value):
        """
        Безопасный ввод:
        - ждём видимость
        - кликаем
        - очищаем поле (ctrl+a + delete)
        - вводим значение
        """
        logger.info(f"Fill {locator} with {value}")
        el = self.wait.until(EC.visibility_of_element_located(locator))
        el.click()
        el.send_keys(Keys.CONTROL, "a")
        el.send_keys(Keys.DELETE)
        el.send_keys(value)

    def get_text(self, locator):
        logger.info(f"Get text: {locator}")
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def wait_visible(self, locator):
        logger.info(f"Wait visible: {locator}")
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_exact_url(self, url):
        logger.info(f"Waiting for exact URL: {url}")
        return self.wait.until(EC.url_to_be(url))
