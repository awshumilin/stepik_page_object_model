from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, "span.btn-group a.btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_FORM1 = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_FORM2 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_FORM3 = (By.CSS_SELECTOR, "#id_registration-password2")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_FORM1 = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_FORM2 = (By.CSS_SELECTOR, "#id_login-password")
    REGISTRATION_BUTTON = (By.NAME, "registration_submit")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    ITEM_ADDED = (By.CSS_SELECTOR, "div.product_main h1")
    PRICE = (By.CSS_SELECTOR, "div.product_main p")
    MESSAGE_ITEM_ADDED = (By.CSS_SELECTOR, "div.alertinner strong")
    MESSAGE_PRICE = (By.CSS_SELECTOR, "div.alertinner p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner p")

class BasketPageLocators():
    ITEM_IN_BASKET = (By.CSS_SELECTOR, "#basket_formset")
    EMPTY_MASSAGE = (By.CSS_SELECTOR, "#content_inner p")


