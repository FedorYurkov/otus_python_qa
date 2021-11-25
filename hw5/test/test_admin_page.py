# -*- coding: utf-8 -*-

def test_admin_page_elements(app):
    admin_page = app.open_admin_page()

    admin_page.assert_element(admin_page._LOGO)
    admin_page.assert_element(admin_page._FORM_TITLE)
    admin_page.assert_element(admin_page._USERNAME_FIELD)
    admin_page.assert_element(admin_page._PASSWORD_FIELD)
    admin_page.assert_element(admin_page._LOGIN_BUTTON)
