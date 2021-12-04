# -*- coding: utf-8 -*-
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    _MAIN_NAV_BAR = (By.CSS_SELECTOR, "#top")

    def __init__(self, app):
        self.driver = app.driver
        self.wait = WebDriverWait(self.driver, 10)

    def assert_element(self, locator, special_timeout=None):
        if special_timeout:
            wait = WebDriverWait(self.driver, special_timeout)
        else:
            wait = self.wait

        try:
            wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"Не дождался видимости элемента: {locator}")
