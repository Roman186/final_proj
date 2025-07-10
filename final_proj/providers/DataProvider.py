import json

my_file = open('./tests/test_data.json')
global_data = json.load(my_file)


class DataProvider:

    def __init__(self) -> None:
        self.data = global_data

    def get_headers(self) -> dict:
        return self.data.get("my_headers")

    def get_params(self) -> dict:
        return self.data.get("params")

    def get_data(self) -> dict:
        return self.data.get("data")
