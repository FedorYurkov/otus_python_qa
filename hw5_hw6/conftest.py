# -*- coding: utf-8 -*-

import logging
from datetime import datetime

import allure
import pytest
from selenium import webdriver

from hw5_hw6.application.app import App


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--url", action="store", default="https://demo.opencart.com")
    parser.addoption("--log_level", action="store", default="INFO")
    parser.addoption("--executor", action="store", default="local")
    parser.addoption("--vnc", action="store_true", default=True)


def driver_factory(browser, executor, vnc):
    if executor == "local":
        if browser == "chrome":
            driver = webdriver.Chrome()
        elif browser == "firefox":
            driver = webdriver.Firefox()
        elif browser == "opera":
            driver = webdriver.Opera()
        else:
            raise Exception("Browser not supported")
    else:
        executor_url = f"http://{executor}:4444/wd/hub"
        caps = {
            "browserName": browser,
            "selenoid:options": {
                "enableVNC": vnc
            }
        }
        driver = webdriver.Remote(
            command_executor=executor_url,
            desired_capabilities=caps
        )

    driver.maximize_window()
    return driver


@pytest.fixture
def app(request):
    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    vnc = request.config.getoption("--vnc")

    driver = driver_factory(browser, executor, vnc)
    url = request.config.getoption("--url")
    log_level = request.config.getoption("--log_level")

    logger = logging.getLogger('driver')
    test_name = request.node.name
    if "\\" in test_name:
        test_name = test_name.split("\\")[0]
    log_path = f"logs/{test_name}_{datetime.now().strftime('%d-%m-%Y_%H.%M.%S')}.log"

    logger.addHandler(logging.FileHandler(log_path))
    logger.setLevel(level=log_level)
    logger.info(f"{logger.name} ===> Test {test_name} started at {datetime.now()}")

    driver.test_name = test_name
    driver.log_level = log_level
    driver.log_path = log_path
    logger.info(f"Browser: {request.config.getoption('--browser')} {driver.desired_capabilities}")

    application = App(driver=driver, base_url=url)

    def fin():
        driver.quit()
        logger.info(f"{logger.name} ===> Test {test_name} finished at {datetime.now()}")

    request.addfinalizer(fin)
    return application


def pytest_exception_interact(node):
    if "app" in node.funcargs:
        allure.attach(
            body=node.funcargs["app"].driver.get_screenshot_as_png(),
            name="screenshot_image",
            attachment_type=allure.attachment_type.PNG
        )
