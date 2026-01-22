import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.epic("Яндекс.Самокат")
@allure.feature("Заказ самоката")
class TestOrderFlow:
    
    # Тестовые данные
    TEST_DATA = [
        {
            "order_button": "top",
            "name": "Иван",
            "last_name": "Иванов",
            "address": "ул. Ленина, д. 10",
            "phone": "+79991234567",
            "date": "15.12.2024",
            "color": "black",
            "comment": "Позвонить за час до доставки"
        },
        {
            "order_button": "bottom",
            "name": "Мария",
            "last_name": "Петрова",
            "address": "пр. Мира, д. 25",
            "phone": "+79997654321",
            "date": "20.12.2024",
            "color": "grey",
            "comment": ""
        }
    ]
    
    @allure.title("Заказ самоката через {order_button} кнопку")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("test_data", TEST_DATA, ids=["top_button", "bottom_button"])
    def test_successful_order(self, driver, test_data):
        # Открываем главную страницу
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.accept_cookies()
        
        # Нажимаем кнопку заказа
        if test_data["order_button"] == "top":
            main_page.click_top_order_button()
        else:
            main_page.click_bottom_order_button()
        
        # Переходим на OrderPage
        order_page = OrderPage(driver)
        
        # Заполняем информацию о заказчике (метод УЖЕ нажимает "Далее" внутри себя)
        order_page.fill_customer_info(
            name=test_data["name"],
            last_name=test_data["last_name"],
            address=test_data["address"],
            phone=test_data["phone"]
        )
        # НЕ вызываем click_next_button() - он уже в fill_customer_info
        
        # Заполняем информацию об аренде
        order_page.fill_rental_info(
            date=test_data["date"],
            color=test_data["color"]
        )
        
        # Оформляем заказ (метод place_order делает всё: клик на кнопку и подтверждение)
        result = order_page.place_order()
        
        # Проверяем успешность
        assert result, "Заказ не был успешно оформлен"
    
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
        
        # Сохраняем текущее окно
        main_window = driver.current_window_handle
        
        # Кликаем на логотип Яндекса
        main_page.click_yandex_logo()
        
        # Ждем открытия нового окна
        WebDriverWait(driver, 10).until(
            lambda d: len(d.window_handles) > 1
        )
        
        # Переключаемся на новое окно
        new_window = [window for window in driver.window_handles if window != main_window][0]
        driver.switch_to.window(new_window)
        
        # Ждем загрузки Дзена
        WebDriverWait(driver, 10).until(
            EC.url_contains("dzen.ru")
        )
        
        # Проверяем URL
        assert "dzen.ru" in driver.current_url