import requests

url = "https://playground.learnqa.ru/ajax/api/compare_query_type"

response = requests.get(url)
print("1) Запрос без параметра: " + response.text, response.status_code)

response = requests.head(url)
print("2) Запрос с методом не из списка HEAD: " + response.text, response.status_code)

response = requests.get(url, params={"method": "GET"})
print("3) Правильное сочетание метода и параметра GET: " + response.text, response.status_code)

response = requests.post(url, data={"method": "POST"})
print("3) Правильное сочетание метода и параметра POST: " + response.text, response.status_code)

methods = [requests.get, requests.post, requests.put, requests.delete, requests.head]
params = ["GET", "POST", "PUT", "DELETE", "HEAD"]

for method in methods:
    for param in params:
        if method == requests.get:
            response = method(url, params={"method": param})
        else:
            response = method(url, data={"method": param})

        print(method, param, response.status_code, response.text)
