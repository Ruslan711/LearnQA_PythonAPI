from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions
import pytest


class TestUserRegister(BaseCase):
    def test_create_user_successfully(self):
        data = self.prepare_registration_data()

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 200)

    def test_create_user_with_existing_email(self):
        email = "vinkotov@example.com"
        data = self.prepare_registration_data(email)
        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", \
            f"Unexpected response content {response.content}"

    # Некорректный email без @
    def test_create_user_incorrect_email(self):
        data = self.prepare_registration_data(email="learnqaru")

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert "Invalid email format" in response.text, \
                f"Unexpected response text: {response.text}"

    # Нет обязательных полей через parametrize
    @pytest.mark.parametrize("missing_field", ["password", "username", "firstName", "lastName", "email"])
    def test_create_user_without_one_field(self, missing_field):
        data = self.prepare_registration_data()
        data.pop(missing_field)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        expected_text = f"The following required params are missed: {missing_field}"
        assert response.text == expected_text, \
            f"Unexpected response text: {response.text}"

    # короткое имя 1 символ
    def test_create_user_with_short_name(self):
        short_name = "a"
        data = self.prepare_registration_data()
        data["firstName"] = short_name

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert "The value of 'firstName' field is too short" in response.text, \
            f"Unexpected response text: {response.text}"

    # Очень длинное имя >250 символов
    def test_create_user_with_long_name(self):
        long_name = "a" * 251
        data = self.prepare_registration_data()
        data["firstName"] = long_name

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert "The value of 'firstName' field is too long" in response.text, \
             f"Unexpected response text: {response.text}"
