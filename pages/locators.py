from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    EXIT = (By.CSS_SELECTOR, "#logout_link")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR,"#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR,"#login_form")
    REG_FORM = (By.CSS_SELECTOR,"#register_form")
    REG_LOGIN = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASS = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_PASS_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_CONFIRM = (By.NAME, "registration_submit")

class ProductPageLocators():
    ADD_PRODUCT = (By.CSS_SELECTOR,"#add_to_basket_form")
    PRODUCT_NAME_VALID = (By.CSS_SELECTOR,"div.col-sm-6.product_main > h1")
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR,"#messages > div:nth-child(1) > div > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR,"#messages > div:nth-child(1)")

class BasketPageLocators():
    BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner > p > a")
    BASKET_PRODUCT_NONE = (By.CSS_SELECTOR,"basket-items")
    BASKET_LINK = (By.CSS_SELECTOR, "span > a")