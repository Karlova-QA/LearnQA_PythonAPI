import pytest
import requests

class TestCookie:
    def test_check_cookie(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")

        cookies = response.cookies
        for cookie in cookies:
            print(f"Cookie name: {cookie.name}, Cookie value: {cookie.value}")

        expected_cookie_name = 'HomeWork'
        expected_cookie_value = 'hw_value'

        assert expected_cookie_name in cookies, "Cookie is missing or its name is not equal HomeWork"
        assert cookies.get(expected_cookie_name) == expected_cookie_value, "Cookie is missing or its name is not equal hw_value"
