import requests

response_any = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
print('1.', response_any.text)

params = {"method": "head"}
response_head = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type", params = params)
print('2.', response_head.headers)

params1 = {"method": "GET"}
response_get = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params = params1)
print('3.', response_get.text)

methods = ["GET", "POST", "PUT", "DELETE"]
for i in methods:
    get1 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params = {"method": {i}})
    print('4.', get1.text, "GET-запрос с методом", i)
    post1 = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data = {"method": {i}})
    print(post1.text, "POST-запрос с методом", i)
    put1 = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", params = {"method": {i}})
    print(put1.text, "PUT-запрос с методом", i)
    delete1 = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", params = {"method": {i}})
    print(delete1.text, "DELETE-запрос с методом", i)









