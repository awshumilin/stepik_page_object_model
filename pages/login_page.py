from .base_page import BasePage
from .locators import LoginPageLocators



class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Not login url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"

    def register_new_user(self, email, password):
        email_link = self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM1)
        email_link.send_keys(email)
        password_link1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM2)
        password_link1.send_keys(password)
        password_link2 = self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM3)
        password_link2.send_keys(password)
        reg_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        reg_button.click()


