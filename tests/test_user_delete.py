from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions


class TestUserDelete(BaseCase):

    def test_delete_protected_user_id_2(self):
        # делаю авторизацию под пользователем id которого будет 2
        login_data = {
            "email": "vinkotov@example.com",
            "password": "1234"
        }
        response1 = MyRequests.post("/user/login", data=login_data)
        Assertions.assert_code_status(response1, 200)

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id = self.get_json_value(response1, "user_id")
        assert user_id == 2

        response2 = MyRequests.delete(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_code_status(response2, 400)
        assert "Please, do not delete test users with ID 1, 2, 3, 4 or 5." in response2.text

    def test_delete_new_user_positive(self):
        # Регистрирую  нового пользователя
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)
        Assertions.assert_code_status(response1, 200)
        user_id = self.get_json_value(response1, "id")

        login_data = {
            "email": register_data["email"],
            "password": register_data["password"]
        }
        response2 = MyRequests.post("/user/login", data=login_data)
        Assertions.assert_code_status(response2, 200)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # Удаляю этого пользователя
        response3 = MyRequests.delete(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )
        Assertions.assert_code_status(response3, 200)

        response4 = MyRequests.get(
            f"/user/{user_id}"
        )

        Assertions.assert_code_status(response4, 404)
        assert "User not found" in response4.text

    def test_delete_user_auth_as_another_user(self):
        # регистрирую  пользователя которого буду пытаться удалить
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)
        Assertions.assert_code_status(response1, 200)
        user_id = self.get_json_value(response1, "id")

        login_data = {
            "email": "vinkotov@example.com",
            "password": "1234"
        }
        response2 = MyRequests.post("/user/login", data=login_data)
        Assertions.assert_code_status(response2, 200)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        response3 = MyRequests.delete(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_code_status(response3, 400)
        response4 = MyRequests.get(f"/user/{user_id}")
        Assertions.assert_code_status(response4, 200)
        Assertions.assert_json_has_key(response4, "username")
