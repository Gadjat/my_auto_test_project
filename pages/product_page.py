from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def go_to_add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_PRODUCT)
        button.click()

    def asertion_add_to_basket(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_VALID).text
        product_name_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET).text
        assert product_name == product_name_in_basket, f'Invalid name in basket({product_name_in_basket})'