from selenium import webdriver
import pytest
import allure
import requests
from final_proj.providers.ConfigProvider import ConfigProvider
from final_proj.providers.DataProvider import DataProvider


@pytest.fixture
def driver():
    """
        Инициализирует webdriver. Запускает браузер.
        После выполнения теста закрывает браузер.
    """

    url = ConfigProvider().get_ui_url()
    browser_name = ConfigProvider().use_browser()

    if browser_name == "chrome":
        with allure.step("Запустить браузер Chrome"):
            driver = webdriver.Chrome()

    else:
        with allure.step("Запустить браузер Edge"):
            driver = webdriver.Edge()

    driver.maximize_window()
    driver.get(url)

    yield driver

    with allure.step("Закрыть браузер"):
        driver.quit()


@pytest.fixture
def get_id_product() -> str:
    """
    Получает id товара
    """
    url = ConfigProvider().get_api_url()
    headers = DataProvider().get_headers()
    params = DataProvider().get_params()
    resp = requests.get(url, params=params, headers=headers)
    id_item = resp.json()['included'][0]['id']

    return id_item
