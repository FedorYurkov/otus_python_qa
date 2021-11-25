# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from hw5.application.pages.base_page import BasePage


class UserAuthPage(BasePage):

    _FORM_TITLE = (By.CSS_SELECTOR, "#content h1")
    _LOGIN_LINK_IN_FORM = (By.CSS_SELECTOR, "#content a[href*='route=account/login']")
    _PERSONAL_DETAILS_SECTION = (By.CSS_SELECTOR, "#account")
    _AGREE_CHECKBOX = (By.CSS_SELECTOR, "[name='agree']")

    def __init__(self, app):
        super().__init__(app)
