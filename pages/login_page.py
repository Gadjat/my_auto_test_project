from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def register_new_user(self, email, password):
        email_form = self.browser.find_element(*LoginPageLocators.REG_LOGIN)
        email_form.send_keys(email)
        pass_form1 = self.browser.find_element(*LoginPageLocators.REG_PASS)
        pass_form1.send_keys(password)
        pass_form2 = self.browser.find_element(*LoginPageLocators.REG_PASS_CONFIRM)
        pass_form2.send_keys(password)
        button_conf = self.browser.find_element(*LoginPageLocators.BUTTON_CONFIRM)
        button_conf.click()

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