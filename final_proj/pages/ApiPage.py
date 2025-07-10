import requests
import copy
import re
from final_proj.providers.ConfigProvider import ConfigProvider
from final_proj.providers.DataProvider import DataProvider


class ApiPage:

    def __init__(self):
        self.url = ConfigProvider().get_api_url()
        self.headers = DataProvider().get_headers()
        self.params = DataProvider().get_params()
        self.body = DataProvider().get_data()

    def latin_letter(self) -> tuple:
        """
        Поиск товара на латинице
        :return: tuple
        """

        resp = requests.get(self.url, params=self.params, headers=self.headers)
        latin_name = resp.json()['included'][0]['attributes']['title']

        return resp, bool(re.search(r'[a-zA-Z]', latin_name))

    def upper_letter(self) -> tuple:
        """
        Поиск товара только в верхнем регистре
        :return: tuple
        """

        original_params = self.params

        new_params = copy.deepcopy(original_params)
        new_params["phrase"] = "ПРОГРАММИРОВАНИЕ"

        resp = requests.get(self.url, params=new_params, headers=self.headers)
        id_item = resp.json()['included'][0]['id']

        return resp, id_item

    def search_two_symbol(self) -> tuple:
        """
        Поиск товара только в верхнем регистре
        :return: tuple
        """

        original_params = self.params

        new_params = copy.deepcopy(original_params)
        new_params["phrase"] = "Ян"

        resp = requests.get(self.url, params=new_params, headers=self.headers)

        id_item = resp.json()['included'][0]['id']

        return resp, id_item

    def wrong_text(self) -> requests.models.Response:
        """
        Поиск товара с ошибкой в названии
        """

        original_params = DataProvider().get_params()

        new_params = copy.deepcopy(original_params)
        new_params["phrase"] = "корандаш"

        resp = requests.get(self.url, params=new_params, headers=self.headers)

        return resp

    def search_for_id(self, id_product) -> tuple:
        """
        Поиск товара по id
        :return: tuple
        """

        original_params = DataProvider().get_params()

        new_params = copy.deepcopy(original_params)
        new_params["phrase"] = f"{id_product}"

        resp = requests.get(self.url, params=new_params, headers=self.headers)

        id_item = resp.json()['included'][0]['id']

        return resp, id_item

    def cyrillic_latin_letter(self) -> tuple:
        """
        Одновременно кириллица и латиница в названии товара
        :return: tuple
        """

        original_params = self.params

        new_params = copy.deepcopy(original_params)
        new_params["phrase"] = "love is жевательная резинка"

        resp = requests.get(self.url, params=new_params, headers=self.headers)

        cyrillic_pattern = r'[а-яА-ЯёЁ]'
        latin_pattern = r'[a-zA-Z]'

        name = resp.json()['included'][0]['attributes']['title']

        has_cyrillic = bool(re.search(cyrillic_pattern, name))
        has_latin = bool(re.search(latin_pattern, name))

        return resp, has_latin, has_cyrillic

    def empty_token(self) -> requests.models.Response:
        """
        Поиск без токена
        """

        original_headers = self.headers

        new_headers = copy.deepcopy(original_headers)
        new_headers['Authorization'] = ''

        resp = requests.get(self.url, params=self.params, headers=new_headers)

        return resp

    def invalid_token(self) -> requests.models.Response:
        """
        Поиск с неправильным токеном
        """

        original_headers = self.headers

        new_headers = copy.deepcopy(original_headers)
        new_headers['Authorization'] = (
            'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.'
            'eyJpc3MiiOj'
        )

        resp = requests.get(self.url, params=self.params, headers=new_headers)

        return resp

    def empty_field(self) -> tuple:
        """
        Пустое поле в строке поиска
        """

        original_params = self.params

        new_params = copy.deepcopy(original_params)
        new_params["phrase"] = ""

        resp = requests.get(self.url, params=new_params, headers=self.headers)
        result = resp.json()

        return resp, result

    def send_smile(self) -> tuple:
        """
        Смайл в строке поиска
        """

        original_params = self.params

        new_params = copy.deepcopy(original_params)
        new_params["phrase"] = "😁😁😁"

        resp = requests.get(self.url, params=new_params, headers=self.headers)
        result = resp.json()

        return resp, result

    def one_symbol(self) -> tuple:
        """
        Поиск с одним символов в строке
        """

        original_params = self.params

        new_params = copy.deepcopy(original_params)
        new_params["phrase"] = "Я"

        resp = requests.get(self.url, params=new_params, headers=self.headers)
        result = resp.json()

        return resp, result

    def text_126_symbols(self) -> tuple:
        """
        126 символов в строке поиска
        """

        original_params = self.params

        new_params = copy.deepcopy(original_params)
        new_params["phrase"] = (
            "Lorem ipsum dolor sits amet, consectetuer adipiscing elit. "
            "Aenean commodo ligula eget dolor. Aenean massadsads. "
            "Cum sociis natoque p"
        )

        resp = requests.get(self.url, params=new_params, headers=self.headers)
        result = resp.json()

        return resp, result

    def search_post_method(self) -> requests.models.Response:
        """
        Поиск методом POST
        """

        resp = requests.post(self.url, json=self.body, headers=self.headers)

        return resp
