import requests
import json
import time

get = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
get_json = get.json()

token = get_json['token']
seconds = get_json['seconds']
print("1.","Token = " , token, "Seconds = ", seconds)

get_before = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job",  params = {"token":token})
get_before_json = get_before.json()
status = get_before_json['status']
if 'status' == "Job is NOT ready":
    print("2.", "Значение поля status верное")
else:
    print("2.", "Значение поля status неверное")
time.sleep(seconds)
get_after = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params = {"token":token})
get_after_json = get_after.json()
result = get_after_json['result']
print(get_after.text)
if 'result' in get_after_json:
    print("3.", "ОК, поле result есть")
else:
    print("3.", "Не ОК, поля result нет")




