from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User


class UserRegisteationTest(APITestCase):
    def test_registration(self):
        url = reverse("user_view")
        user_data = {
            "username":"gracia",
            "fullname":"graciadivina",
            "email":"gracia@gmail.com",
            "password":"divina"
        }
        response = self.client.post(url, user_data)
        print(response.data)