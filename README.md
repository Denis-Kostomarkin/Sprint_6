# Yandex Scooter — UI Test Automation

Учебный проект по автоматизации UI-тестирования сервиса «Яндекс Самокат».

> **Статус:** тесты разработаны для учебного окружения. Доступность стенда и актуальные результаты запуска не подтверждены.

## Стек
- Python
- Selenium WebDriver
- Pytest
- Allure Pytest
- Page Object Model

## Сценарии
- Проверка ответов на восемь вопросов раздела «Вопросы о важном» (параметризация Pytest).
- Оформление заказа через верхнюю и нижнюю кнопки «Заказать».
- Переход по логотипу Самоката.
- Переход по логотипу Яндекса.

## Структура
```text
Sprint_6/
├── pages/
│   ├── base_page.py
│   ├── main_page.py
│   └── order_page.py
├── tests/
│   ├── test_order_flow.py
│   └── test_questions.py
├── conftest.py
├── requirements.txt
└── README.md
```

## Установка
```bash
git clone https://github.com/Denis-Kostomarkin/Sprint_6.git
cd Sprint_6
python -m venv .venv
```

Windows PowerShell:
```powershell
.\.venv\Scripts\Activate.ps1
```

Linux / macOS:
```bash
source .venv/bin/activate
```

```bash
pip install -r requirements.txt
```

## Запуск
```bash
pytest tests/ -v
```

Для сбора результатов Allure:
```bash
pytest tests/ --alluredir=allure-results
```

При установленном Allure CLI:
```bash
allure serve allure-results
```

## Особенности реализации
- Page Object Model для разделения тестов и логики страниц.
- Фикстура Pytest для настройки и закрытия браузера.
- Параметризация тестов FAQ.
- Allure-аннотации сценариев.

## Автор
[Denis-Kostomarkin](https://github.com/Denis-Kostomarkin)
