import pytest
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.epic("Яндекс.Самокат")
@allure.feature("Заказ самоката")
class TestOrderFlow:
    
    TEST_DATA = [
        {
            "button": "top",
            "name": "Иван",
            "last_name": "Иванов",
            "address": "ул. Ленина, д. 10",
            "phone": "+79991234567",
            "date": "15.12.2024",
            "color": "black"
        },
        {
            "button": "bottom",
            "name": "Мария",
            "last_name": "Петрова",
            "address": "пр. Мира, д. 25",
            "phone": "+79997654321",
            "date": "20.12.2024",
            "color": "grey"
        }
    ]
    
    @allure.title("Заказ самоката")
    @pytest.mark.parametrize("data", TEST_DATA)
    def test_successful_order(self, main_page, data):
        if data["button"] == "top":
            order_page = main_page.click_order_button_top()
        else:
            order_page = main_page.click_order_button_bottom()
        
        order_page.fill_customer_info(
            data["name"], data["last_name"], data["address"], data["phone"]
        )
        order_page.fill_rental_info(data["date"], data["color"])
        
        assert order_page.place_order()
    
    @allure.title("Переход по логотипу Самоката")
    def test_scooter_logo_redirect(self, main_page):
        main_page.click_scooter_logo()
        assert "qa-scooter" in main_page.get_current_url()
    
    @allure.title("Переход по логотипу Яндекса")
    def test_yandex_logo_redirect(self, main_page):
        main_window = main_page.driver.current_window_handle
        main_page.click_yandex_logo()
        
        WebDriverWait(main_page.driver, 10).until(
            lambda d: len(d.window_handles) > 1
        )
        
        new_window = [w for w in main_page.driver.window_handles if w != main_window][0]
        main_page.driver.switch_to.window(new_window)
        
        WebDriverWait(main_page.driver, 10).until(
            EC.url_contains("dzen.ru")
        )
        assert "dzen.ru" in main_page.driver.current_url