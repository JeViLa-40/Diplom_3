from pages.base_page import BasePage
from locators.locators_feed_page import LocatorsFeedPage
from urls import Urls
import allure


class FeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открываем страницу Лента Заказов')
    def open_feed_page(self):
        self.open_page(Urls.FEED_URL)

    @allure.step('Кликаем по кнопке Конструктор в шапке')
    def click_on_button_constructor(self):
        self.click_on_element_with_wait(LocatorsFeedPage.BUTTON_CONSTRUCTOR)

    @allure.step('Находим заголовок Лента заказов для проверки успешного перехода')
    def find_header_feed_orders(self):
        return self.find_element_with_wait(LocatorsFeedPage.HEADER_FEED_ORDERS)

    @allure.step('Находим количество выполненных за все время заказов')
    def find_counter_all_orders_done(self):
        return self.find_element_with_wait(LocatorsFeedPage.COUNTER_ALL_ORDERS_DONE)

    @allure.step('Находим количество выполненных за сегодня заказов')
    def find_counter_today_orders_done(self):
        return self.find_element_with_wait(LocatorsFeedPage.COUNTER_TODAY_ORDERS_DONE)

    @allure.step('Находим заказ в работе')
    def find_order_in_progress(self):
        return self.find_element_with_wait_for_change_element(LocatorsFeedPage.ORDER_IN_PROGRESS, 'Все текущие заказы готовы!')
