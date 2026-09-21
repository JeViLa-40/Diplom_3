from selenium.webdriver.common.by import By

class LocatorsConstructorPage:
    BUTTON_FEED = [By.XPATH, './/p[text()="Лента Заказов"]']
    INGREDIENT_CARD_FLUOR_BUN = [By.XPATH, './/*[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]']
    CROSS_WINDOW_INGREDIENT_DETAILS = [By.CSS_SELECTOR, '.Modal_modal_opened__3ISw4 .Modal_modal__close_modified__3V5XS']
    HEADER_ASSEMBLE_BURGER = [By.XPATH, './/h1[text()="Соберите бургер"]']
    HEADER_INGREDIENTS_DETAILS = [By.XPATH, './/h2[text()="Детали ингредиента"]']
    BASKET = [By.XPATH, './/span[@class="constructor-element__text"]']
    COUNTER_INGREDIENT_SAUCE_SPICY = [By.XPATH,'.//*[@href="/ingredient/61c0c5a71d1f82001bdaaa72"]//p[@class="counter_counter__num__3nue1"]']
    BUTTON_PLACE_ORDER = [By.XPATH, './/button[text()="Оформить заказ"]']
    CROSS_WINDOW_ORDER = [By.CSS_SELECTOR, '.Modal_modal__close_modified__3V5XS.Modal_modal__close__TnseK']
    ORDER_NUMBER = [By.CSS_SELECTOR, '.Modal_modal__title_shadow__3ikwq']
    INGREDIENT_CARD_SPICY_SAUCE = [By.XPATH, './/*[@href="/ingredient/61c0c5a71d1f82001bdaaa72"]']
