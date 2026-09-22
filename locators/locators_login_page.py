from selenium.webdriver.common.by import By

class LocatorsLoginPage:
    BUTTON_LOGIN = [By.CSS_SELECTOR, '.button_button__33qZ0']
    EMAIL_FIELD = [By.XPATH, './/input[@name="name"]']
    PASSWORD_FIELD = [By.XPATH, './/input[@name="Пароль"]']
