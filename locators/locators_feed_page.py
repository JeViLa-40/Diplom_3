from selenium.webdriver.common.by import By

class LocatorsFeedPage:
    BUTTON_CONSTRUCTOR = [By.XPATH, './/p[text()="Конструктор"]']
    HEADER_FEED_ORDERS = [By.XPATH, '//h1[text()="Лента заказов"]']
    COUNTER_ALL_ORDERS_DONE = [By.XPATH, './/div[@class="undefined mb-15"]/p[@class="OrderFeed_number__2MbrQ text text_type_digits-large"]']
    COUNTER_TODAY_ORDERS_DONE = [By.XPATH, './/p[text()="Выполнено за сегодня:"]/../p[contains(@class, "text_type_digits-large")]']
    ORDER_IN_PROGRESS = [By.XPATH, './/ul[contains(@class, "OrderFeed_orderListReady__1YFem")]/li']
