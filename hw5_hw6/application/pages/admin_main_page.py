# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from hw5_hw6.application.pages.base_page import BasePage


class AdminMainPage(BasePage):

    _CATALOG_MENU_ITEM = (By.CSS_SELECTOR, "#menu-catalog")
    _PRODUCTS_MENU_ITEM = (By.XPATH, "//a[.='Products']")

    def __init__(self, app):
        super().__init__(app)

    def open_admin_products_page(self):
        self.driver.find_element(*self._CATALOG_MENU_ITEM).click()
        self.driver.find_element(*self._PRODUCTS_MENU_ITEM).click()
