# -*- coding: utf-8 -*-
import logging

from hw5_hw6.application.pages.admin_auth_page import AdminPage
from hw5_hw6.application.pages.catalog_page import CatalogPage
from hw5_hw6.application.pages.main_page import MainPage
from hw5_hw6.application.pages.product_page import ProductPage
from hw5_hw6.application.pages.user_auth_page import UserAuthPage


class App:

    def __init__(self, driver, base_url):
        self.driver = driver
        self.driver.implicitly_wait(3)
        self.base_url = base_url

        self.__config_logger()

        self.main_page = None
        self.catalog_page = None
        self.product_page = None
        self.admin_page = None
        self.user_auth_page = None

    def __config_logger(self):
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.addHandler(logging.FileHandler(self.driver.log_path))
        self.logger.setLevel(level=self.driver.log_level)

    def open_main_page(self):
        self.logger.info(f"{self.logger.name}: Opening url: {self.base_url}")
        self.driver.get(self.base_url)
        if not self.main_page:
            self.main_page = MainPage(self)
        return self.main_page

    def open_catalog_page(self, category_id=20):
        self.logger.info(f"{self.logger.name}: Opening url: {self.base_url}/index.php?route=product/category&path={category_id}")
        self.driver.get(self.base_url + f"/index.php?route=product/category&path={category_id}")
        if not self.catalog_page:
            self.catalog_page = CatalogPage(self)
            self.catalog_page.category_id = category_id
        return self.catalog_page

    def open_product_page(self, product_id=43):
        self.logger.info(f"{self.logger.name}: Opening url: {self.base_url}/index.php?route=product/product&product_id={product_id}")
        self.driver.get(self.base_url + f"/index.php?route=product/product&product_id={product_id}")
        if not self.product_page:
            self.product_page = ProductPage(self)
            self.product_page.product_id = product_id
        return self.product_page

    def open_admin_page(self):
        self.logger.info(f"{self.logger.name}: Opening url: {self.base_url}/admin/")
        self.driver.get(self.base_url + "/admin/")
        if not self.admin_page:
            self.admin_page = AdminPage(self)
        return self.admin_page

    def open_user_auth_page(self):
        self.logger.info(f"{self.logger.name}: Opening url: {self.base_url}/index.php?route=account/register")
        self.driver.get(self.base_url + "/index.php?route=account/register")
        if not self.user_auth_page:
            self.user_auth_page = UserAuthPage(self)
        return self.user_auth_page
