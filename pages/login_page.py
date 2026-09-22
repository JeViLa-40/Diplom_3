from pages.base_page import BasePage
from locators.locators_login_page import LocatorsLoginPage
from locators.locators_constructor_page import LocatorsConstructorPage
from urls import Urls
import allure


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открываем страницу авторизации')
    def open_login_page(self):
        self.open_page(Urls.LOGIN_URL)

    @allure.step('Авторизуем пользователя')
    def login_user(self, email, password):
        self.fill_field(LocatorsLoginPage.EMAIL_FIELD, email)
        self.fill_field(LocatorsLoginPage.PASSWORD_FIELD, password)
        self.click_on_element_with_wait(LocatorsLoginPage.BUTTON_LOGIN)
        self.find_element_with_wait(LocatorsConstructorPage.HEADER_ASSEMBLE_BURGER)
