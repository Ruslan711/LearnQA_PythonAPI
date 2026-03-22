import requests
import time

url = "https://playground.learnqa.ru/ajax/api/longtime_job"

create_task = requests.get(url)
parsed_response_text = create_task.json()
print(parsed_response_text)

token_value = parsed_response_text["token"]
seconds_value = parsed_response_text["seconds"]

request_with_token = requests.get(url, params={"token": token_value})
parsed_before = request_with_token.json()
print(parsed_before)

time.sleep(seconds_value)

request_task_complete = requests.get(url, params={"token": token_value})
parsed_after = request_task_complete.json()
print(parsed_after)
