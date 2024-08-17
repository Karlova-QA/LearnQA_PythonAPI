import pytest
import requests

class TestLength:

    def test_check_length(self):

        phrase = input("Set a phrase: ")

        assert len(phrase) < 15, "The phrase length is greater than or equal to 15 characters"

