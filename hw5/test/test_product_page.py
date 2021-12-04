# -*- coding: utf-8 -*-


def test_product_page_elements(app):
    product_page = app.open_product_page()

    product_page.assert_element(product_page._PRODUCT_TITLE)
    product_page.assert_element(product_page._ADD_TO_CART_BUTTON)
    product_page.assert_element(product_page._PHOTOS)
    product_page.assert_element(product_page._PRODUCT_NAV_BAR)
    product_page.assert_element(product_page._RATING_BLOCK)
