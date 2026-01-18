from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import allure


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://qa-scooter.praktikum-services.ru/"
    
    @allure.step("Открыть главную страницу")
    def open(self):
        self.driver.get(self.url)
        return self
    
    @allure.step("Принять куки")
    def accept_cookies(self):
        try:
            cookie_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()
        except:
            pass
        return self
    
    ORDER_BUTTON_TOP = (By.XPATH, "//button[text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "(//button[text()='Заказать'])[2]")
    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    
    QUESTIONS = {
        0: (By.ID, "accordion__heading-0"),
        1: (By.ID, "accordion__heading-1"),
        2: (By.ID, "accordion__heading-2"),
        3: (By.ID, "accordion__heading-3"),
        4: (By.ID, "accordion__heading-4"),
        5: (By.ID, "accordion__heading-5"),
        6: (By.ID, "accordion__heading-6"),
        7: (By.ID, "accordion__heading-7"),
    }
    
    ANSWERS = {
        0: (By.ID, "accordion__panel-0"),
        1: (By.ID, "accordion__panel-1"),
        2: (By.ID, "accordion__panel-2"),
        3: (By.ID, "accordion__panel-3"),
        4: (By.ID, "accordion__panel-4"),
        5: (By.ID, "accordion__panel-5"),
        6: (By.ID, "accordion__panel-6"),
        7: (By.ID, "accordion__panel-7"),
    }
    
    EXPECTED_ANSWERS = {
        0: "Сутки — 400 рублей. Оплата курьеру — наличными или картой.",
        1: "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.",
        2: "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.",
        3: "Только начиная с завтрашнего дня. Но скоро станем расторопнее.",
        4: "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.",
        5: "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.",
        6: "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.",
        7: "Да, обязательно. Всем самокатов! И Москве, и Московской области."
    }
    
    @allure.step("Нажать на вопрос номер {question_num}")
    def click_question(self, question_num):
        question = self.driver.find_element(*self.QUESTIONS[question_num])
        self.driver.execute_script("arguments[0].scrollIntoView();", question)
        question.click()
    
    @allure.step("Получить текст ответа на вопрос {question_num}")
    def get_answer_text(self, question_num):
        answer = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.ANSWERS[question_num])
        )
        return answer.text
    
    @allure.step("Нажать верхнюю кнопку 'Заказать'")
    def click_order_button_top(self):
        self.driver.find_element(*self.ORDER_BUTTON_TOP).click()
        from pages.order_page import OrderPage
        return OrderPage(self.driver)
    
    @allure.step("Нажать нижнюю кнопку 'Заказать'")
    def click_order_button_bottom(self):
        button = self.driver.find_element(*self.ORDER_BUTTON_BOTTOM)
        self.driver.execute_script("arguments[0].scrollIntoView();", button)
        button.click()
        from pages.order_page import OrderPage
        return OrderPage(self.driver)
    
    @allure.step("Нажать на логотип Самоката")
    def click_scooter_logo(self):
        self.driver.find_element(*self.SCOOTER_LOGO).click()
    
    @allure.step("Нажать на логотип Яндекса")
    def click_yandex_logo(self):
        self.driver.find_element(*self.YANDEX_LOGO).click()
    
    def get_current_url(self):
        return self.driver.current_url