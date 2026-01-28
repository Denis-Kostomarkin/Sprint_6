import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.epic("Яндекс.Самокат")
@allure.feature("Заказ самоката")
class TestOrderFlow:
    
    TOP_BUTTON_DATA = {
        "name": "Иван",
        "last_name": "Иванов",
        "address": "ул. Ленина, д. 10",
        "phone": "+79991234567",
        "date": "15.12.2024",
        "color": "black",
        "comment": "Позвонить за час до доставки"
    }
    
    BOTTOM_BUTTON_DATA = {
        "name": "Мария",
        "last_name": "Петрова",
        "address": "пр. Мира, д. 25",
        "phone": "+79997654321",
        "date": "20.12.2024",
        "color": "grey",
        "comment": ""
    }
    
    @allure.title("Заказ самоката через верхнюю кнопку")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_successful_order_top_button(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.accept_cookies()
        
        main_page.click_order_button_top()
        
        order_page = OrderPage(driver)
        order_page.fill_customer_info(
            self.TOP_BUTTON_DATA["name"],
            self.TOP_BUTTON_DATA["last_name"],
            self.TOP_BUTTON_DATA["address"],
            self.TOP_BUTTON_DATA["phone"]
        )
        order_page.fill_rental_info(
            self.TOP_BUTTON_DATA["date"],
            self.TOP_BUTTON_DATA["color"]
        )
        
        assert order_page.place_order()
    
    @allure.title("Заказ самоката через нижнюю кнопку")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_successful_order_bottom_button(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.accept_cookies()
        
        main_page.click_order_button_bottom()
        
        order_page = OrderPage(driver)
        order_page.fill_customer_info(
            self.BOTTOM_BUTTON_DATA["name"],
            self.BOTTOM_BUTTON_DATA["last_name"],
            self.BOTTOM_BUTTON_DATA["address"],
            self.BOTTOM_BUTTON_DATA["phone"]
        )
        order_page.fill_rental_info(
            self.BOTTOM_BUTTON_DATA["date"],
            self.BOTTOM_BUTTON_DATA["color"]
        )
        
        assert order_page.place_order()
    
    @allure.title("Переход на главную через логотип Самоката")
    @allure.severity(allure.severity_level.NORMAL)
    def test_scooter_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.accept_cookies()
        
        main_page.click_scooter_logo()
        
        current_url = main_page.get_current_url()
        assert "qa-scooter" in current_url
    
    @allure.title("Переход на Дзен через логотип Яндекса")
    @allure.severity(allure.severity_level.NORMAL)
    def test_yandex_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.accept_cookies()
        
        main_window = driver.current_window_handle
        main_page.click_yandex_logo()
        
        main_page.wait.until(
            lambda d: len(d.window_handles) > 1
        )
        
        new_window = [window for window in driver.window_handles if window != main_window][0]
        driver.switch_to.window(new_window)
        
        main_page.wait.until(
            EC.url_contains("dzen.ru")
        )
        
        assert "dzen.ru" in main_page.get_current_url()