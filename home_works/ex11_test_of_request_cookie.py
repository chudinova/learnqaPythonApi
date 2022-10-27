import requests


def test_of_request_cookie():
    response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
    assert response.cookies.get("HomeWork") == "hw_value"
