from pages.constructor_page import ConstructorPage
from pages.feed_page import FeedPage
import allure


class TestFeedPage:

    @allure.title('Проверка перехода на страницу конструктора по клику на кнопку Конструктор в шапке')
    def test_click_on_button_constructor(self, driver):
        feed_page = FeedPage(driver)
        feed_page.open_page()
        feed_page.click_on_button_constructor()
        constructor_page = ConstructorPage(driver)
        header = constructor_page.find_header_assemble_burger()
        assert header.text == "Соберите бургер", "Текст заголовка не соответствует ожидаемому"
   
    @allure.title('Проверка увеличения счетчика "Выполнено за всё время" при создании нового заказа')
    def test_increase_counter_all_orders_done(self, driver):
        feed_page = FeedPage(driver)
        feed_page.open_page()
        number_before = feed_page.find_counter_all_orders_done().text
        feed_page.click_on_button_constructor()
        constructor_page = ConstructorPage(driver)
        constructor_page.place_order()
        constructor_page.click_on_cross_to_close_window_order()
        constructor_page.click_on_button_feed()
        number_after = feed_page.find_counter_all_orders_done().text
        assert int(number_after) == int(number_before) + 1
