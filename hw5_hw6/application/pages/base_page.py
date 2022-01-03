# -*- coding: utf-8 -*-
import logging

import allure
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    _MAIN_NAV_BAR = (By.CSS_SELECTOR, "#top")
    _MAIN_NAV_BAR_CURRENCY = (By.CSS_SELECTOR, "#form-currency button[data-toggle='dropdown']")
    _CURRENCY_MENU_ITEM_EUR = (By.CSS_SELECTOR, "#form-currency button[name='EUR']")
    _CURRENCY_MENU_ITEM_GBP = (By.CSS_SELECTOR, "#form-currency button[name='GBP']")
    _CURRENCY_MENU_ITEM_USD = (By.CSS_SELECTOR, "#form-currency button[name='USD']")

    # General methods

    def __init__(self, app):
        self.driver = app.driver
        self.wait = WebDriverWait(self.driver, 15)
        self.__config_logger()

    def __config_logger(self):
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.addHandler(logging.FileHandler(self.driver.log_path))
        self.logger.setLevel(level=self.driver.log_level)

    def assert_element(self, locator, special_timeout=None):
        self.logger.info(f"{self.logger.name}: Assert element: {locator} with special_timeout {special_timeout}")
        if special_timeout:
            wait = WebDriverWait(self.driver, special_timeout)
        else:
            wait = self.wait

        try:
            wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"Не дождался видимости элемента: {locator}")

    def type(self, locator, value):
        self.logger.info(f"{self.logger.name}: Type '{value}' to element: {locator}")
        field = self.driver.find_element(*locator)
        current_value_in_field = field.get_attribute("value")
        if current_value_in_field != value:
            field.click()
            if current_value_in_field != '':
                field.clear()
            field.send_keys(value)
        return self

    def is_displayed(self, locator, context=None):
        self.logger.info(f"{self.logger.name}: Assert is element displayed: {locator} with context {context}")
        if not context:
            context = self.driver
        try:
            return context.find_element(*locator).is_displayed()
        except NoSuchElementException:
            return False

    # Methods of working with MAIN NAV BAR

    @allure.step("Switch currency to: {to}")
    def switch_currency_in_main_nav(self, to):
        self.logger.info(f"{self.logger.name}: Switch currency to: {to}")
        if to == "EUR":
            locator = self._CURRENCY_MENU_ITEM_EUR
        elif to == "GBP":
            locator = self._CURRENCY_MENU_ITEM_GBP
        elif to == "USD":
            locator = self._CURRENCY_MENU_ITEM_USD
        else:
            raise RuntimeError("Unsupported currency!")

        self.driver.find_element(*self._MAIN_NAV_BAR_CURRENCY).click()
        self.driver.find_element(*locator).click()

        return self

    @allure.step("Get currency text")
    def get_currency_text_from_main_nav(self):
        self.logger.info(f"{self.logger.name}: Get currency text")
        return self.driver.find_element(*self._MAIN_NAV_BAR_CURRENCY).text
