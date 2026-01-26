from selenium.webdriver.common.by import By
from .base_page import BasePage
import allure


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://qa-scooter.praktikum-services.ru/"
    
    # Локаторы
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    ORDER_BUTTON_TOP = (By.XPATH, "//button[text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "(//button[text()='Заказать'])[2]")
    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    
    # Локаторы вопросов по ID (стабильные)
    QUESTION_LOCATORS = [
        (By.ID, "accordion__heading-0"),
        (By.ID, "accordion__heading-1"),
        (By.ID, "accordion__heading-2"),
        (By.ID, "accordion__heading-3"),
        (By.ID, "accordion__heading-4"),
        (By.ID, "accordion__heading-5"),
        (By.ID, "accordion__heading-6"),
        (By.ID, "accordion__heading-7"),
    ]
    
    # Ожидаемые тексты ответов
    EXPECTED_ANSWERS = [
        "Сутки — 400 рублей. Оплата курьеру — наличными или картой.",
        "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.",
        "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.",
        "Только начиная с завтрашнего дня. Но скоро станем расторопнее.",
        "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.",
        "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.",
        "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.",
        "Да, обязательно. Всем самокатов! И Москве, и Московской области."
    ]
    
    @allure.step("Открыть главную страницу")
    def open_main_page(self):
        self.go_to(self.url)
        return self
    
    @allure.step("Принять куки")
    def accept_cookies(self):
        if self.is_visible(self.COOKIE_BUTTON, timeout=3):
            self.click(self.COOKIE_BUTTON)
        return self
    
    @allure.step("Нажать на вопрос {question_index}")
    def click_question(self, question_index):
        """Кликнуть на вопрос по индексу (0-7)"""
        if 0 <= question_index <= 7:
            self.scroll_to(self.QUESTION_LOCATORS[question_index])
            self.click(self.QUESTION_LOCATORS[question_index])
        else:
            raise ValueError("Индекс вопроса должен быть от 0 до 7")
        return self
    
    @allure.step("Получить текст ответа на вопрос {question_index}")
    def get_answer_text(self, question_index):
        """Получить текст ответа по индексу (0-7)"""
        if 0 <= question_index <= 7:
            answer_locator = (By.ID, f"accordion__panel-{question_index}")
            return self.get_text(answer_locator)
        else:
            raise ValueError("Индекс вопроса должен быть от 0 до 7")
    
    @allure.step("Нажать верхнюю кнопку 'Заказать'")
    def click_order_button_top(self):
        self.click(self.ORDER_BUTTON_TOP)
        return self
    
    @allure.step("Нажать нижнюю кнопку 'Заказать'")
    def click_order_button_bottom(self):
        self.scroll_to(self.ORDER_BUTTON_BOTTOM)
        self.click(self.ORDER_BUTTON_BOTTOM)
        return self
    
    @allure.step("Нажать на логотип Самоката")
    def click_scooter_logo(self):
        self.click(self.SCOOTER_LOGO)
        return self
    
    @allure.step("Нажать на логотип Яндекса")
    def click_yandex_logo(self):
        self.click(self.YANDEX_LOGO)
        return self