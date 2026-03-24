import requests


def test_get_cookie():
    url = "https://playground.learnqa.ru/api/homework_cookie"
    response = requests.get(url)

    print(response.cookies)

    cookie_value = response.cookies.get("HomeWork")

    assert cookie_value is not None
    assert cookie_value == "hw_value"
