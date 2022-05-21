from selenium.webdriver.common.by import By


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