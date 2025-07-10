from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import re


class Main:
    def __init__(self, driver):
        self.driver = driver
        self.field_search_locator = ("xpath", "//input[@type='text']")
        self.items_locator = (
            "xpath",
            "//article[@class='product-card app-products-list__item']"
        )
        self.submit_button_locator = ("xpath", "//button[@type='submit']")

    def search_display(self) -> bool:
        """
        Находит строку поиска товаров на странице
        :return: bool
        """
        field_display = self.driver.find_element(
            *self.field_search_locator).is_displayed()

        return field_display

    def placeholder(self) -> str:
        """
        Находит название маски в строке поиска товаров
        :return: str
        """
        placeholder_text = self.driver.find_element(
            *self.field_search_locator).get_attribute("placeholder")

        return placeholder_text

    def search_product(self, query: str) -> list:
        """
        Общий метод для поиска товаров
        :return: list
        """
        search_field = self.driver.find_element(*self.field_search_locator)

        search_field.send_keys(Keys.CONTROL + "a")
        search_field.send_keys(Keys.DELETE)

        search_field.send_keys(query)

        submit_button = WebDriverWait(self.driver, 7).until(
            EC.element_to_be_clickable(self.submit_button_locator)
        )
        submit_button.click()

        try:
            return WebDriverWait(self.driver, 25).until(
                EC.visibility_of_all_elements_located(self.items_locator)
            )
        except TimeoutException:
            return []

    def get_first_product_name(self) -> str:
        """
        Получение названия первого товара в результатах
        :return: str
        """
        elements = self.search_product("")

        if elements:
            return elements[0].find_element(
                "xpath",
                "//a[@class='product-card__title']"
            ).text
        return ""

    def get_first_product_id(self) -> str:
        """
        Получение ID первого товара в результатах
        :return: str
        """
        elements = self.search_product("")
        link = elements[0].find_element(
            "xpath",
            "//article[@class='product-card app-products-list__item'][1]//a"
        )
        self.driver.execute_script("arguments[0].click();", link)

        locator_product = (
            "xpath",
            "//li[contains(., 'ID товара')]//span[2]/span"
        )
        element = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(locator_product))

        id_product = element.text

        if elements:
            return id_product
        return ""

    def latin_letters(self) -> bool:
        """
        Поиск товара на латинице
        :return: bool
        """
        self.search_product("programming")
        latin_name = self.get_first_product_name()

        return bool(re.search(r'[a-zA-Z]', latin_name))

    def russian_letters(self) -> bool:
        """
        Поиск товара на кириллице
        :return: bool
        """
        self.search_product("азбука")
        russian_name = self.get_first_product_name()

        return bool(re.search(r'[а-яА-Я]', russian_name))

    def digit_letter(self) -> bool:
        """
        Поиск товара цифрами
        :return: bool
        """
        self.search_product("123")
        name = self.get_first_product_name()
        is_digit_present = any(character.isdigit() for character in name)

        return is_digit_present

    def search_for_id(self, product_id: str) -> str:
        """
        Поиск товара по ID
        :return: str
        """
        self.search_product(product_id)

        return self.get_first_product_id()

    def search_non_exist_product(self) -> str:
        """
        Поиск несуществующего товара
        :return: str
        """
        self.search_product("йцууйцвыавмаив")

        try:
            return WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(
                    ("xpath", "//h4[@class='catalog-stub__title']")
                )).text
        except TimeoutException:
            return ""

    def only_space_in_field(self) -> bool:
        """
        Вводит только пробелы в поле поиска товара
        :return: bool
        """
        self.search_product("    ")

        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(
                    ("xpath", "//h1[@class='search-title']")))

            return False
        except TimeoutException:
            return True

    def empty_field(self) -> bool:
        """
        Поиск с пустым значением
        :return: bool
        """
        self.search_product("")

        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(
                    ("xpath", "//h1[@class='search-title']")
                ))

            return False
        except TimeoutException:
            return True

    def get_id_by_name(self, name: str) -> str:
        """
        Получает ID товара по названию
        :return: str
        """
        self.search_product(name)
        return self.get_first_product_id()

    def space_before_after_text(self) -> str:
        """
        Получает текст заголовка в результате поиска товара
        :return: str
        """
        self.search_product("  азбука  ")

        text_title = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(
                ("xpath", "//h1[@class='search-title']")
            )).text

        return text_title
