from pages.base_page import BasePage
from locators.locators_constructor_page import LocatorsConstructorPage
from urls import Urls
import allure

class ConstructorPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открываем страницу конструктора')
    def open_page(self):
        self.driver.get(Urls.CONSTRUCTOR_URL)

    @allure.step('Кликаем по кнопке Лента Заказов в шапке')
    def click_on_button_feed(self):
        self.click_on_element_with_wait(LocatorsConstructorPage.BUTTON_FEED)

    @allure.step('Кликаем по ингредиенту Флюоресцентная булка')
    def click_on_card_fluor_bun(self):
        self.click_on_element_with_wait(LocatorsConstructorPage.INGREDIENT_CARD_FLUOR_BUN)

    @allure.step('Кликаем на крестик в окне Детали ингредиента')
    def click_on_cross_to_close_window_ingredient(self):
        self.click_on_element_with_wait(LocatorsConstructorPage.CROSS_WINDOW_INGREDIENT_DETAILS)

    @allure.step('Находим заголовок Соберите бургер для проверки успешного перехода')
    def find_header_assemble_burger(self):
        return self.find_element_with_wait(LocatorsConstructorPage.HEADER_ASSEMBLE_BURGER)

    @allure.step('Находим заголовок для проверки появления окна Детали ингредиента')
    def find_header_ingredient_details(self):
        return self.find_element_with_wait(LocatorsConstructorPage.HEADER_INGREDIENTS_DETAILS)

    @allure.step('Находим счетчик ингредиента соус Спайси')
    def find_counter_ingredient_sauce_spicy(self):
        return self.find_element_with_wait(LocatorsConstructorPage.COUNTER_INGREDIENT_SAUCE_SPICY)

    @allure.step('Кликаем по кнопке Оформить заказ')
    def click_on_button_place_order(self):
        self.click_on_element_with_wait(LocatorsConstructorPage.BUTTON_PLACE_ORDER)

    @allure.step('Кликаем на крестик в окне заказа')
    def click_on_cross_to_close_window_order(self):
        self.click_on_element_with_wait(LocatorsConstructorPage.CROSS_WINDOW_ORDER)

    """def click_on_cross_to_close_window_order(self):
    # Оставляем ваше ожидание, чтобы элемент точно был в DOM и доступен
    cross_button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable(self.CROSS_LOCATOR) # используйте ваш локатор
    )
    # Вместо cross_button.click() пишем:
    self.driver.execute_script("arguments[0].click();", cross_button)
"""


    @allure.step('Находим номер заказа в окне заказа')
    def find_order_number(self):
        return self.find_element_with_wait(LocatorsConstructorPage.ORDER_NUMBER)

    @allure.step('Ожидаем закрытие окна с деталями заказа')
    def wait_for_close_ingredient_details_window(self):
        self.wait_for_invisibility_of_element_located(LocatorsConstructorPage.HEADER_INGREDIENTS_DETAILS)

    @allure.step('Добавляем соус в корзину')
    def drag_sauce_to_basket(self):
        self.drag_and_drop(LocatorsConstructorPage.INGREDIENT_CARD_SPICY_SAUCE, LocatorsConstructorPage.BASKET)

    @allure.step('Создаем заказ')
    def place_order(self):
        self.drag_and_drop(LocatorsConstructorPage.INGREDIENT_CARD_FLUOR_BUN, LocatorsConstructorPage.BASKET)
        self.drag_sauce_to_basket()
        self.click_on_button_place_order()

