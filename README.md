# Selenium-Python-Example

Этот репозиторий содержит базовую настройку проекта тестирования пользовательского интерфейса с использованием шаблона Python, Selenium Webdriver и Page Object Model.

В качестве примера используется простой поиск в DuckDuckGo для проверки отображения результатов.

# Требования

* Python 3.7.X
* pip и setuptools
* [venv](<https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/>) (рекомендуется)

# Установка

1. Скачайте или клонируйте репозиторий
2. Откройте терминал
3. Перейдите в корневой каталог проекта "/PythonSeleniumExample3/".
4. Создайте виртуальную среду: `py -m venv venv`
5. Активируйте виртуальную среду, выполнив следующий скрипт: `.\venv\Scripts\activate`
6. Выполните следующую команду, чтобы загрузить необходимые библиотеки:  `pip install -r requirements.txt`

# Выполнение теста

1. Откройте терминал
2. Из корневого каталога проекта запустите: `pytest -v --html=results/report.html`

# Конфигурация

По умолчанию тесты будут выполняться в Chrome (обычный режим). Предпочтения можно изменить в файле "/data/config.yaml"

# Результаты

Чтобы проверить отчет, откройте файл '/results/report.html' после завершения выполнения.


# Ссылки
   
   [Selenium - Python Documentation](<https://selenium-python.readthedocs.io/>)
   
   [Webdriver Manager for Python](<https://github.com/SergeyPirogov/webdriver_manager>)
   
   