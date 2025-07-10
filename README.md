# final_proj

Проект содержит автоматизированные тесты для веб-приложения с использованием Selenium WebDriver и Allure для генерации отчетов.

## Предварительные требования

1. Установите **Python 3.8** или новее
2. Установите браузер **Chrome**
3. Установите **WebDriver** для браузера (устанавливаются автоматически через selenium)
4. Перед выполнением тестов зайти на [сайт](https://www.chitai-gorod.ru), открыть Devtools, взять значение **access-token**
5. В значение ключа `"Authorization"` вставить полученный **access-token** (файл `test_data.json`)


## Структура проекта

```
final_proj/
├── final_proj/             # Основной код проекта
│   ├── pages/                 
│   ├── ApiPage.py
│   ├── MainPage.py
│   ├── providers/          # Директория для провайдеров
├── ├── ConfigProvider.py            
│   └── DataProvider.py
│
├── tests/                  # Тесты
│   ├── conftest.py         # Фикстуры для pytest
│   ├── test_api.py
│   ├── test_config.ini     # Конфигурационный файл
│   ├── test_data.json      # Тестовые данные
│   └── test_ui.py     
│
├── .gitignore              # Список неотслеживаемых файлов
├── pytest.ini              # Конфигурация Pytest
├── README.md               # Документация проекта (этот файл)
└── requirements.txt        # Python зависимости

```

### Шаги

1. Склонировать проект: `git clone https://github.com/Roman186/final_proj.git`
2. Установить необходимые зависимости: `pip install -r requirements.txt`
3. Перейдите в рабочую директорию: `cd <название директории>`
4. Запустите тесты с генерацией данных для отчета: `pytest --alluredir allure-result`
* После выполнения в директории проекта появится папка **allure-result** с результатами тестов.

### Просмотр отчета

Для просмотра отчета выполните команду: `allure serve allure-result`

1. Откроется новая вкладка браузера с отчетом
2. Отчет будет содержать: общую статистику по тестам, детализацию по каждому тесту, графики и характеристики
3. Для остановки сервера нажмите `Ctr+C` в терминале
4. Для сохранения отчета в статическом формате выполните: `allure generate allure-result -o allure-report`

### Дополнительная информация

1. [Подсказка по markdown](https://www.markdownguide.org/basic-syntax/)
2. Для работы Allure должен быть установлен глобально
3. [Подсказка по allure](https://allurereport.org/docs/pytest/)
4. [Документация pytest](https://docs.pytest.org/en/stable/getting-started.html)
5. Добавления / изменения тестовых данных вносить в файл `test_data.json`
6. Добавления / изменения конфигурационных данных вносить в файл `test_config.ini`
7. Для конфигурации Pytest редактировать файл `pytest.ini`
