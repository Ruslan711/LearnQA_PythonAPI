import requests


def test_get_header():
    url = "https://playground.learnqa.ru/api/homework_header"
    response = requests.get(url)

    print(response.headers)

    header_value = response.headers.get("x-secret-homework-header")

    assert header_value is not None
    assert header_value == "Some secret value"
