from pages.constructor_page import ConstructorPage
from pages.feed_page import FeedPage
import allure


class TestConstructorPage:

    @allure.title('Проверка перехода на страницу Лента заказов по клику на кнопку Лента заказов в шапке')
    def test_click_on_button_feed(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.open_constructor_page()
        constructor_page.click_on_button_feed()
        feed_page = FeedPage(driver)
        header = feed_page.find_header_feed_orders()
        assert header.text == "Лента заказов", "Текст заголовка не соответствует ожидаемому"

    @allure.title('Проверка появления окна с деталями ингредиента при клике на него')
    def test_click_on_ingredient(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.open_constructor_page()
        constructor_page.click_on_card_fluor_bun()
        header = constructor_page.find_header_ingredient_details()
        assert header.text == "Детали ингредиента", "Текст заголовка не соответствует ожидаемому"

    @allure.title('Проверка закрытия окна с деталями ингредиента по клику на крестик')
    def test_click_on_cross_window_ingredient_details(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.open_constructor_page()
        constructor_page.click_on_card_fluor_bun()
        header = constructor_page.find_header_ingredient_details()
        constructor_page.click_on_cross_to_close_window_ingredient()
        constructor_page.wait_for_close_ingredient_details_window()
        assert not header.is_displayed()

    @allure.title('Проверка увеличения счетчика ингредиента при добавлении его в заказ')
    def test_increase_counter_ingredient(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.open_constructor_page()
        count_before = constructor_page.find_counter_ingredient_sauce_spicy().text
        constructor_page.drag_sauce_to_basket()
        count_after = constructor_page.find_counter_ingredient_sauce_spicy().text
        assert int(count_after) == int(count_before) + 1
