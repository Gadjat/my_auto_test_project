from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def go_to_basket_page(self):
        link = self.browser.find_element(*BasketPageLocators.BASKET_LINK)
        link.click()

    def should_be_basket_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY), "Basket_empty message is presented"

    def basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCT_NONE), "Basket empty"
