from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        link_login = self.browser.current_url
        # реализуйте проверку на корректный url адрес
        assert "login" in link_login, f"'login' is not {link_login} "

    def should_be_login_form(self):
        self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"# реализуйте проверку, что есть форма логина
        assert True

    def should_be_register_form(self):
        self.is_element_present(*LoginPageLocators.REG_FORM), "Registration form is not presented"# реализуйте проверку, что есть форма регистрации на странице
        assert True