from selenium.webdriver.common.by import By
from .base_page import BasePage
import allure


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://qa-scooter.praktikum-services.ru/"
    
    # Локаторы
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    
    # Кнопки заказа - находим по родительским блокам
    ORDER_BUTTON_TOP = (By.XPATH, "//div[contains(@class, 'Header')]//button[text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]//button[text()='Заказать']")
    
    # Логотипы
    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    
    # Вопросы и ответы - находим по data-атрибутам или тексту
    QUESTION_LOCATOR = (By.XPATH, "//div[@data-accordion-component='AccordionItemButton']")
    ANSWER_LOCATOR = (By.XPATH, "//div[@data-accordion-component='AccordionItemPanel']")
    
    # Список ожидаемых текстов ответов
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
        self.open(self.url)
        return self
    
    @allure.step("Принять куки")
    def accept_cookies(self):
        if self.is_element_visible(self.COOKIE_BUTTON, timeout=3):
            self.click_element(self.COOKIE_BUTTON)
        return self
    
    @allure.step("Нажать на вопрос по индексу {index}")
    def click_question_by_index(self, index):
        """Кликнуть на вопрос по порядковому номеру (0-based)"""
        all_questions = self.driver.find_elements(*self.QUESTION_LOCATOR)
        if index < len(all_questions):
            self.scroll_to_element((By.ID, all_questions[index].get_attribute("id")))
            all_questions[index].click()
        else:
            raise IndexError(f"Вопрос с индексом {index} не найден. Всего вопросов: {len(all_questions)}")
        return self
    
    @allure.step("Получить текст ответа по индексу {index}")
    def get_answer_text_by_index(self, index):
        """Получить текст ответа по порядковому номеру (0-based)"""
        all_answers = self.driver.find_elements(*self.ANSWER_LOCATOR)
        if index < len(all_answers):
            return all_answers[index].text
        else:
            raise IndexError(f"Ответ с индексом {index} не найден. Всего ответов: {len(all_answers)}")
    
    @allure.step("Нажать верхнюю кнопку 'Заказать'")
    def click_top_order_button(self):
        self.scroll_to_element(self.ORDER_BUTTON_TOP)
        self.click_element(self.ORDER_BUTTON_TOP)
        return self
    
    @allure.step("Нажать нижнюю кнопку 'Заказать'")
    def click_bottom_order_button(self):
        self.scroll_to_element(self.ORDER_BUTTON_BOTTOM)
        self.click_element(self.ORDER_BUTTON_BOTTOM)
        return self
    
    @allure.step("Нажать на логотип Самоката")
    def click_scooter_logo(self):
        self.click_element(self.SCOOTER_LOGO)
        return self
    
    @allure.step("Нажать на логотип Яндекса")
    def click_yandex_logo(self):
        self.click_element(self.YANDEX_LOGO)
        return self