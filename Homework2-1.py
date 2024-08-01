import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)

history_length = len(response.history)

print(history_length)
print(response.url)