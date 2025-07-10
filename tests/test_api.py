import pytest
import allure
from final_proj.pages.ApiPage import ApiPage


@pytest.mark.API
@pytest.mark.Positive
@allure.title("API. Поиск товара на латинице")
@allure.description("Запрос на поиск товара латиницей")
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.NORMAL)
def test_latin_letter():
    api_page = ApiPage()
    latin_letter = api_page.latin_letter()
    status_code = latin_letter[0].status_code

    assert status_code == 200, \
        f"Ожидаемый статус-код: 200, в итоге: {status_code}"
    assert latin_letter[1] is True, "В названии товара нет латинских букв"


@pytest.mark.API
@pytest.mark.Positive
@allure.title("API. Поиск в верхнем регистре")
@allure.description("Запрос на поиск товара в верхнем регистре")
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.NORMAL)
def test_upper_letter():
    api_page = ApiPage()
    upper_letter = api_page.upper_letter()
    status_code = upper_letter[0].status_code

    assert status_code == 200, \
        f"Ожидаемый статус-код: 200, в итоге: {status_code}"
    assert len(upper_letter[1]) > 0, "Товар не найден"


@pytest.mark.API
@pytest.mark.Positive
@allure.title("API. Минимальное количество символов в поле поиска")
@allure.description("Проверка минимальной границы поля: 2 символа")
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.NORMAL)
def test_search_two_symbol():
    api_page = ApiPage()
    two_symbol = api_page.search_two_symbol()
    status_code = two_symbol[0].status_code

    assert status_code == 200, \
        f"Ожидаемый статус-код: 200, в итоге: {status_code}"
    assert len(two_symbol[1]) > 0, "Товар не найден"


@pytest.mark.API
@pytest.mark.Positive
@allure.title("API. Поиск товара с ошибкой в названии")
@allure.description("Проверка обработки ошибок в названии товаров")
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.NORMAL)
def test_wrong_text():
    api_page = ApiPage()
    two_symbol = api_page.wrong_text()
    status_code = two_symbol.status_code

    assert status_code == 200, \
        f"Ожидаемый статус-код: 200, в итоге: {status_code}"


@pytest.mark.API
@pytest.mark.Positive
@allure.title("API. Поиск по id товара")
@allure.description("Проверка поиска товара по его id")
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.NORMAL)
def test_search_for_id(get_id_product):
    api_page = ApiPage()
    product = api_page.search_for_id(get_id_product)
    status_code = product[0].status_code

    assert status_code == 200, \
        f"Ожидаемый статус-код: 200, в итоге: {status_code}"
    assert get_id_product == product[1], \
        "id полученного товара != id в строке поиска"


@pytest.mark.API
@pytest.mark.Positive
@allure.title("API. Смешанный ввод")
@allure.description("Проверка комбинации кириллицы и латиницы в тексте")
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.NORMAL)
def test_cyrillic_latin_together():
    api_page = ApiPage()
    result = api_page.cyrillic_latin_letter()
    status_code = result[0].status_code

    assert status_code == 200, \
        f"Ожидаемый статус-код: 200, в итоге: {status_code}"
    assert result[1] is True, "В названии товара нет латиницы"
    assert result[2] is True, "В названии товара нет кириллицы"


@pytest.mark.API
@pytest.mark.Negative
@allure.title("API. Пустой токен")
@allure.description("Проверка запроса с пустым токеном")
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_empty_token():
    api_page = ApiPage()
    result = api_page.empty_token()
    status_code = result.status_code

    assert result.status_code == 401, \
        f"Ожидаемый статус-код: 401, в итоге: {status_code}"


@pytest.mark.API
@pytest.mark.Negative
@allure.title("API. Некорректный токен")
@allure.description("Проверка запроса с некорректным токеном")
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_invalid_token():
    api_page = ApiPage()
    result = api_page.invalid_token()
    status_code = result.status_code

    assert result.status_code == 401, \
        f"Ожидаемый статус-код: 401, в итоге: {status_code}"


@pytest.mark.API
@pytest.mark.Negative
@allure.title("API. Пустое значение в запросе")
@allure.description("Проверка запроса с пустым значением")
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.MINOR)
def test_empty_field():
    api_page = ApiPage()
    result = api_page.empty_field()
    status_code = result[0].status_code

    assert status_code == 400, \
        f"Ожидаемый статус-код: 400, в итоге: {status_code}"
    assert 'errors' in result[1], "В ответе не приходит ошибка"


@pytest.mark.API
@pytest.mark.Negative
@allure.title("API. Запрос со смайликами")
@allure.description("Проверка запроса с смайлами")
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.MINOR)
def test_send_smile():
    api_page = ApiPage()
    result = api_page.send_smile()
    status_code = result[0].status_code

    assert status_code == 422, \
        f"Ожидаемый статус-код: 422, в итоге: {status_code}"
    assert 'errors' in result[1], "В ответе не приходит ошибка"


@pytest.mark.API
@pytest.mark.Negative
@allure.title("API. Нарушение минимальной границы поля поиска")
@allure.description("Количество символов в поле: 1")
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.NORMAL)
def test_one_symbol():
    api_page = ApiPage()
    result = api_page.one_symbol()
    status_code = result[0].status_code
    assert status_code == 400, \
        f"Ожидаемый статус-код: 400, в итоге: {status_code}"
    assert 'errors' in result[1], "В ответе не приходит ошибка"


@pytest.mark.API
@pytest.mark.Negative
@allure.title("API. Нарушение максимальной границы поля поиска")
@allure.description("Количество символов в поле: 126")
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.NORMAL)
def test_126_symbols():
    api_page = ApiPage()
    result = api_page.text_126_symbols()
    status_code = result[0].status_code
    assert status_code == 422, \
        f"Ожидаемый статус-код: 422, в итоге: {status_code}"
    assert 'errors' in result[1], "В ответе не приходит ошибка"


@pytest.mark.API
@pytest.mark.Negative
@allure.title("API. Поиск товаров другим http методом")
@allure.description("Запрос методом POST")
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.NORMAL)
def test_search_post_method():
    api_page = ApiPage()
    result = api_page.search_post_method()
    status_code = result.status_code
    assert status_code == 405, \
        f"Ожидаемый статус-код: 405, в итоге: {status_code}"
