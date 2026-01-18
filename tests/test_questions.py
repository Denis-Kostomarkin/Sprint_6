import pytest
import allure


@allure.epic("Яндекс.Самокат")
@allure.feature("Вопросы о важном")
class TestQuestions:
    
    @allure.title("Проверка ответов на вопросы")
    @pytest.mark.parametrize("question_num", range(8))
    def test_question_answer(self, main_page, question_num):
        main_page.click_question(question_num)
        actual = main_page.get_answer_text(question_num)
        expected = main_page.EXPECTED_ANSWERS[question_num]
        assert actual == expected