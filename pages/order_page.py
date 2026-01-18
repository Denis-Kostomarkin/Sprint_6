from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import allure
import time 


class OrderPage:
    def __init__(self, driver):
        self.driver = driver
    
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
    ORDER_BUTTON = (By.XPATH, "//button[text()='Заказать']")
    
    CONFIRM_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']")
    SUCCESS_MODAL = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]")
    
    @allure.step("Заполнить информацию о заказчике")
    def fill_customer_info(self, name, last_name, address, phone):
        self.driver.find_element(*self.NAME_INPUT).send_keys(name)
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)
        self.driver.find_element(*self.ADDRESS_INPUT).send_keys(address)
        
        metro_field = self.driver.find_element(*self.METRO_INPUT)
        metro_field.click()
        metro_field.send_keys("Сокольники")
        
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.METRO_STATION)
        ).click()
        
        self.driver.find_element(*self.PHONE_INPUT).send_keys(phone)
        self.driver.find_element(*self.NEXT_BUTTON).click()
        return self
    
    @allure.step("Заполнить информацию об аренде")
    def fill_rental_info(self, date, color="black"):
        date_input = self.driver.find_element(*self.DATE_INPUT)
        date_input.click()
        date_input.send_keys(date)
        date_input.send_keys(Keys.ESCAPE)
        
        self.driver.find_element(*self.RENTAL_PERIOD).click()
        self.driver.find_element(*self.RENTAL_1_DAY).click()
        
        if color == "black":
            self.driver.find_element(*self.BLACK_CHECKBOX).click()
        elif color == "grey":
            self.driver.find_element(*self.GREY_CHECKBOX).click()
        
        return self
    
    @allure.step("Оформить заказ")
    def place_order(self):
        try:
            order_button = self.driver.find_element(*self.ORDER_BUTTON)
            order_button.click()
            
            time.sleep(2)
            
            confirm_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.CONFIRM_BUTTON)
            )
            confirm_button.click()
            
            success_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.SUCCESS_MODAL)
            )
            return True
        except Exception as e:
            print(f"Ошибка при оформлении заказа: {e}")
            return False