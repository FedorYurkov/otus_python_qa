# -*- coding: utf-8 -*-
import pytest
import requests

base_url = "https://jsonplaceholder.typicode.com"


@pytest.mark.parametrize("uid", [1, 2, 3, 4])
def test_1(uid):
    response = requests.get(url=f"{base_url}/posts/{uid}")
    assert response.json()["id"] == uid


def test_2():
    response = requests.get(url=f"{base_url}/posts")
    assert len(response.json()) == 100


@pytest.mark.parametrize("title, user_id", [("title_1", 11), ("title_2", 11), ("title_3", 11)])
def test_3(title, user_id):
    response = requests.post(url=f"{base_url}/posts",
                             headers={"Content-type": "application/json; charset=UTF-8"},
                             json={"title": title, "body": "some body", "userId": user_id}
                             )
    r = response.json()
    assert response.status_code == 201
    assert response.json()["title"] == title


def test_4():
    response_before = requests.get(url=f"{base_url}/posts/1")
    response_after = requests.patch(url=f"{base_url}/posts/1",
                                    headers={"Content-type": "application/json; charset=UTF-8"},
                                    json={"title": response_before.json()["title"] + "_edit"}
                                    )
    assert response_after.json()["title"] ==  response_before.json()["title"] + "_edit"


def test_5():
    r = requests.delete(url=f"{base_url}/posts/1")
    assert r.status_code == 200
