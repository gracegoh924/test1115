from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User


class UserRegisteationTest(APITestCase):
    def test_registration(self):
        url = reverse("user_view") # 이 이름에 해당하는 url을 가져온다.
        user_data = {
            "username":"gracia",
            "fullname":"graciadivina",
            "email":"gracia@gmail.com",
            "password":"divina"
        }
        response = self.client.post(url, user_data)
        print(response.data)
        self.assertEqual(response.data["message"], "가입 완료!!")
        # self.assertEqual(response.data, {"message" : "가입 완료!!"})