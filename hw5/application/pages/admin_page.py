# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from hw5.application.pages.base_page import BasePage


class AdminPage(BasePage):
    _LOGO = (By.CSS_SELECTOR, "#header-logo")
    _FORM_TITLE = (By.CSS_SELECTOR, ".panel-title")
    _USERNAME_FIELD = (By.CSS_SELECTOR, "#input-username")
    _PASSWORD_FIELD = (By.CSS_SELECTOR, "#input-password")
    _LOGIN_BUTTON = (By.XPATH, "//button[.=' Login']")

    def __init__(self, app):
        super().__init__(app)
