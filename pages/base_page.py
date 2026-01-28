from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
import logging


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.wait = WebDriverWait(driver, 10)
    
    @allure.step("Найти элемент")
    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    @allure.step("Найти кликабельный элемент")
    def find_clickable_element(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))
    
    @allure.step("Нажать на элемент")
    def click(self, locator):
        element = self.find_clickable_element(locator)
        element.click()
        return element
    
    @allure.step("Ввести текст '{text}'")
    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
        return element
    
    @allure.step("Получить текст элемента")
    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text
    
    @allure.step("Прокрутить к элементу")
    def scroll_to(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        return element
    
    @allure.step("Проверить видимость элемента")
    def is_visible(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except:
            return False
    
    @allure.step("Перейти на URL")
    def go_to(self, url):
        self.driver.get(url)
        return self
    
    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step("Переключиться на окно")
    def switch_to_window(self, window_handle):
        """Переключиться на указанное окно"""
        self.driver.switch_to.window(window_handle)
        return self

    @allure.step("Получить список дескрипторов окон")
    def get_window_handles(self):
        """Получить список всех дескрипторов окон"""
        return self.driver.window_handles

    @allure.step("Получить текущий дескриптор окна")
    def get_current_window_handle(self):
        """Получить дескриптор текущего окна"""
        return self.driver.current_window_handle