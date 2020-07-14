from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR,"#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR,"#login_form")
    REG_FORM = (By.CSS_SELECTOR,"#register_form")

class ProductPageLocators():
    ADD_PRODUCT = (By.CSS_SELECTOR,"#add_to_basket_form")
    PRODUCT_NAME_VALID = (By.CSS_SELECTOR,"div.col-sm-6.product_main > h1")
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR,"#messages > div:nth-child(1) > div > strong")