import requests

#response = requests.get("https://playground.learnqa.ru/api/hello")
#print(response.text)

response1 = requests.get("https://playground.learnqa.ru/api/get_text")
print(response1.text)