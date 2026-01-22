import pytest
import allure
from pages.main_page import MainPage  # Добавить импорт


@allure.epic("Яндекс.Самокат")
@allure.feature("Вопросы о важном")
class TestQuestions:
    
    @allure.title("Проверка ответов на вопросы")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("question_index", range(8))
    def test_question_answer(self, driver, question_index):  # Используем driver вместо main_page
        # Создаем экземпляр MainPage
        main_page = MainPage(driver)
        
        # Открываем страницу и принимаем куки
        main_page.open_main_page()
        main_page.accept_cookies()
        
        # Кликаем на вопрос
        main_page.click_question_by_index(question_index)
        
        # Получаем текст ответа
        actual_answer = main_page.get_answer_text_by_index(question_index)
        
        # Проверяем соответствие ожидаемому тексту
        expected_answer = main_page.EXPECTED_ANSWERS[question_index]
        
        assert actual_answer == expected_answer, \
            f"Неправильный ответ на вопрос {question_index + 1}.\n" \
            f"Ожидалось: {expected_answer}\n" \
            f"Получено: {actual_answer}"