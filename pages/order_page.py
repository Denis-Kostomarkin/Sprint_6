from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from .base_page import BasePage
import allure


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    # Локаторы
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_STATION = (By.XPATH, "//div[text()='Сокольники']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD = (By.XPATH, "//div[text()='* Срок аренды']")
    RENTAL_1_DAY = (By.XPATH, "//div[text()='сутки']")
    BLACK_CHECKBOX = (By.ID, "black")
    GREY_CHECKBOX = (By.ID, "grey")
    ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']")
    
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MODAL = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]")
    
    @allure.step("Заполнить информацию о заказчике")
    def fill_customer_info(self, name, last_name, address, phone):
        self.send_keys(self.NAME_INPUT, name)
        self.send_keys(self.LAST_NAME_INPUT, last_name)
        self.send_keys(self.ADDRESS_INPUT, address)
        
        self.click(self.METRO_INPUT)
        metro_field = self.find_element(self.METRO_INPUT)
        metro_field.send_keys("Сокольники")
        
        self.wait.until(lambda d: self.is_visible(self.METRO_STATION))
        self.click(self.METRO_STATION)
        
        self.send_keys(self.PHONE_INPUT, phone)
        self.click(self.NEXT_BUTTON)
        return self
    
    @allure.step("Заполнить информацию об аренде")
    def fill_rental_info(self, date, color="black"):
        date_element = self.find_clickable_element(self.DATE_INPUT)
        date_element.click()
        date_element.send_keys(date)
        date_element.send_keys(Keys.ESCAPE)
        
        self.click(self.RENTAL_PERIOD)
        self.click(self.RENTAL_1_DAY)
        
        if color == "black":
            self.click(self.BLACK_CHECKBOX)
        elif color == "grey":
            self.click(self.GREY_CHECKBOX)
        
        return self
    
    @allure.step("Оформить заказ")
    def place_order(self):
        self.click(self.ORDER_BUTTON)
        
        # Ожидание без time.sleep
        self.wait.until(lambda d: self.is_visible(self.CONFIRM_BUTTON))
        
        confirm_button = self.find_clickable_element(self.CONFIRM_BUTTON)
        confirm_button.click()
        
        # Проверка успешности без исключений и print
        return self.is_visible(self.SUCCESS_MODAL, timeout=10)