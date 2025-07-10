import pytest
import allure
from final_proj.pages.MainPage import Main


@pytest.mark.UI
@pytest.mark.Positive
@allure.title("UI. Отображение поля поиска товаров")
@allure.description("Проверка отображения поля поиска на странице")
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_search_display(driver):
    main_page = Main(driver)
    search_display = main_page.search_display()

    assert search_display is True, \
        "Строка поиска отсутствует на странице"


@pytest.mark.UI
@pytest.mark.Positive
@allure.title("UI. Отображение маски в поле поиска товаров")
@allure.description("Проверка отображения placeholder в поле поиска")
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.MINOR)
def test_placeholder(driver):
    main_page = Main(driver)
    placeholder = main_page.placeholder()

    assert placeholder and len(placeholder) > 0, \
        "Placeholder отсутствует в поле поиска"


@pytest.mark.UI
@pytest.mark.Positive
@allure.title("UI. Поиск товара на латинице")
@allure.description("Проверка наличия латиницы в названии товара")
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.NORMAL)
def test_latin_letters(driver):
    main_page = Main(driver)
    latin_letter = main_page.latin_letters()

    assert latin_letter is True, \
        "В названии товара нет латинских букв"


@pytest.mark.UI
@pytest.mark.Positive
@allure.title("UI. Поиск товара на кириллице")
@allure.description("Проверка наличия кириллицы в названии товара")
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.NORMAL)
def test_russian_letters(driver):
    main_page = Main(driver)
    russ_name = main_page.russian_letters()

    assert russ_name is True, \
        "В названии товара нет кириллицы"


@pytest.mark.UI
@pytest.mark.Positive
@allure.title("UI. Поиск товара буквами")
@allure.description("Проверка наличия букв названии товара")
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.NORMAL)
def test_digit_letter(driver):
    main_page = Main(driver)
    is_digit = main_page.digit_letter()

    assert is_digit is True, \
        "В названии товара нет букв"


@pytest.mark.UI
@pytest.mark.Positive
@allure.title("UI. Поиск товара по id")
@allure.description("Проверка поиска товара по его id")
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.NORMAL)
def test_search_for_id(driver):
    main_page = Main(driver)
    product_id_before = main_page.get_id_by_name("programming")
    product_id_after = main_page.search_for_id(product_id_before)

    assert product_id_before == product_id_after, \
        "id полученного товара != id в строке поиска"


@pytest.mark.UI
@pytest.mark.Negative
@allure.title("UI. Пустое значение в поиске")
@allure.description("Поиск с пустым значением в поле")
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.MINOR)
def test_empty_field(driver):
    main_page = Main(driver)
    result = main_page.empty_field()

    assert result is True, \
        f"Ожидаемое значение: True, в итоге: {result}"


@pytest.mark.UI
@pytest.mark.Negative
@allure.title("UI. Только пробелы в поле поиска товаров")
@allure.description("Ввод только пробелов в поле поиска")
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.MINOR)
def test_only_space_in_field(driver):
    main_page = Main(driver)
    result = main_page.only_space_in_field()

    assert main_page.only_space_in_field() is True, \
        f"Ожидаемое значение: True, в итоге: {result}"


@pytest.mark.UI
@pytest.mark.Negative
@allure.title("UI. Несуществующий товар")
@allure.description("Поиск несуществующего товара")
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.MINOR)
def test_search_non_exist_product(driver):
    main_page = Main(driver)
    result = main_page.search_non_exist_product()

    assert "Похоже, у нас такого нет" in result, \
        "При поиске несуществующего товара, в результате отображаются товары"


@pytest.mark.UI
@pytest.mark.Negative
@allure.title("UI. Пробелы до и после текста")
@allure.description("Проверка обработки пробелов до текста и после")
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.MINOR)
def test_space_before_after_text(driver):
    main_page = Main(driver)
    title_text = main_page.space_before_after_text()

    assert "азбука" in title_text, \
        "Строка поиска не обрабатывает пробела до и после текста"
