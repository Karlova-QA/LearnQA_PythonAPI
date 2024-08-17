import pytest
import requests
from datetime import datetime, timezone
import time

class TestHeaders:
    def test_check_headers(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_header")

        headers = response.headers

        for header_name, header_value in headers.items():
            print(f"Header name: {header_name}, Header value: {header_value}")

        current_time_utc = datetime.now(timezone.utc)
        date = current_time_utc.strftime('%a, %d %b %Y %H:%M:%S GMT')

        expected_headers = {'Date': date, 'Content-Type': 'application/json', 'Content-Length': '15', 'Connection': 'keep-alive', 'Keep-Alive': 'timeout=10', 'Server': 'Apache', 'x-secret-homework-header': 'Some secret value', 'Cache-Control': 'max-age=0', 'Expires': date}

        assert expected_headers == headers, "Headers are missing or not as expected"




