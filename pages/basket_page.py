from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_massage_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_MASSAGE), "No massage about empty basket"

    def should_be_no_items_in_basket(self):
        assert not self.is_element_present(*BasketPageLocators.ITEM_IN_BASKET), "There is item in basket"
