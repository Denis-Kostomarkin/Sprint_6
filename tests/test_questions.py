import pytest
import allure
from pages.main_page import MainPage


@allure.epic("Яндекс.Самокат")
@allure.feature("Вопросы о важном")
class TestQuestions:
    
    @allure.title("Проверка ответов на вопросы")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("question_index", range(8))
    def test_question_answer(self, driver, question_index):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.accept_cookies()
        
        # Кликаем на вопрос по индексу
        main_page.click_question(question_index)
        
        # Получаем текст ответа
        actual_answer = main_page.get_answer_text(question_index)
        expected_answer = MainPage.EXPECTED_ANSWERS[question_index]
        
        assert actual_answer == expected_answer