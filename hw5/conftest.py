# -*- coding: utf-8 -*-
import pytest
from selenium import webdriver

from hw5.application.app import App


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--url", action="store", default="https://demo.opencart.com")


def driver_factory(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "opera":
        driver = webdriver.Opera()
    else:
        raise Exception("Browser not supported")
    driver.maximize_window()
    return driver


@pytest.fixture
def app(request):
    driver = driver_factory(request.config.getoption("--browser"))
    url = request.config.getoption("--url")
    application = App(driver=driver, base_url=url)
    request.addfinalizer(driver.quit)
    return application
