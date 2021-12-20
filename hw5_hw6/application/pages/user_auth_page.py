# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from hw5_hw6.application.pages.base_page import BasePage


class UserAuthPage(BasePage):

    _CONTENT_TITLE = (By.CSS_SELECTOR, "#content h1")
    _LOGIN_LINK_IN_FORM = (By.CSS_SELECTOR, "#content a[href*='route=account/login']")
    _PERSONAL_DETAILS_SECTION = (By.CSS_SELECTOR, "#account")

    _FIRST_NAME_FIELD = (By.CSS_SELECTOR, "#input-firstname")
    _LAST_NAME_FIELD = (By.CSS_SELECTOR, "#input-lastname")
    _EMAIL_FIELD = (By.CSS_SELECTOR, "#input-email")
    _PHONE_FIELD = (By.CSS_SELECTOR,"#input-telephone")
    _PASSWORD_FIELD = (By.CSS_SELECTOR, "#input-password")
    _PASSWORD_CONFIRM_FIELD = (By.CSS_SELECTOR, "#input-confirm")
    _AGREE_CHECKBOX = (By.CSS_SELECTOR, "[name='agree']")
    _CONTINUE_BUTTON = (By.CSS_SELECTOR, "input[type='submit'][value='Continue']")

    def __init__(self, app):
        super().__init__(app)

    def get_content_title_text(self):
        return self.driver.find_element(*self._CONTENT_TITLE).text

    def fill_first_name(self, value):
        self.type(self._FIRST_NAME_FIELD, value)
        return self

    def fill_last_name(self, value):
        self.type(self._LAST_NAME_FIELD, value)
        return self

    def fill_email(self, value):
        self.type(self._EMAIL_FIELD, value)
        return self

    def fill_phone(self, value):
        self.type(self._PHONE_FIELD, value)
        return self

    def fill_password(self, value):
        self.type(self._PASSWORD_FIELD, value)
        return self

    def fill_password_confirm(self, value):
        self.type(self._PASSWORD_CONFIRM_FIELD, value)
        return self

    def fill_agree_with_privacy_checkbox(self):
        self.driver.find_element(*self._AGREE_CHECKBOX).click()
        return self

    def submit_continue_button(self):
        self.driver.find_element(*self._CONTINUE_BUTTON).click()
