from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def product_add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button is not presented"

    def item_title_is_correct(self):
        assert self.browser.find_element(*ProductPageLocators.ITEM_ADDED).text == self.browser.find_element(*ProductPageLocators.MESSAGE_ITEM_ADDED).text, "Item title is not correct"

    def item_price_is_correct(self):
        assert self.browser.find_element(*ProductPageLocators.PRICE).text == self.browser.find_element(*ProductPageLocators.MESSAGE_PRICE).text, "Item price is not correct"

