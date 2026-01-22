from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import allure
import logging


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.wait = WebDriverWait(driver, 10)
    
    @allure.step("Найти элемент {locator}")
    def find_element(self, locator):
        """Базовый метод для поиска элемента с ожиданием"""
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    @allure.step("Найти кликабельный элемент {locator}")
    def find_clickable_element(self, locator):
        """Базовый метод для поиска кликабельного элемента"""
        return self.wait.until(EC.element_to_be_clickable(locator))
    
    @allure.step("Нажать на элемент {locator}")
    def click_element(self, locator):
        """Базовый метод для клика по элементу"""
        element = self.find_clickable_element(locator)
        element.click()
        return element
    
    @allure.step("Ввести текст '{text}' в элемент {locator}")
    def send_keys_to_element(self, locator, text):
        """Базовый метод для ввода текста"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
        return element
    
    @allure.step("Получить текст элемента {locator}")
    def get_element_text(self, locator):
        """Базовый метод для получения текста элемента"""
        element = self.find_element(locator)
        return element.text
    
    @allure.step("Скроллить к элементу {locator}")
    def scroll_to_element(self, locator):
        """Базовый метод для скролла к элементу"""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        return element
    
    @allure.step("Проверить видимость элемента {locator}")
    def is_element_visible(self, locator, timeout=5):
        """Базовый метод для проверки видимости элемента"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except:
            return False
    
    @allure.step("Перейти на URL {url}")
    def open(self, url):
        """Базовый метод для открытия URL"""
        self.driver.get(url)
        return self
    
    @allure.step("Получить текущий URL")
    def get_current_url(self):
        """Базовый метод для получения текущего URL"""
        return self.driver.current_url