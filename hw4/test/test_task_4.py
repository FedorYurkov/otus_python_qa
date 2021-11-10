# -*- coding: utf-8 -*-
import requests


def test_task_4(url_and_code):
    response = requests.get(url=url_and_code["url"])
    assert str(response.status_code) == url_and_code["status_code"]
