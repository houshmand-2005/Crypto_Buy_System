import json
from django.test import TestCase
from rest_framework.test import APIRequestFactory
from accounts.api.user.create_user import CreateUserAPI
from datetime import datetime


class TestCreateUserAPI(TestCase):
    def test_create_user(self):
        factory = APIRequestFactory()
        data = {
            "user_name": "newuser",
            "password": "newpassword1234",
            "phone_number": "+989018924315",
            "last_login": datetime.now().isoformat(),
            "amount": 10,
            "is_active": True,
            "is_staff": False,
            "is_superuser": False,
        }
        request = factory.post(
            "/create/", json.dumps(data), content_type="application/json"
        )
        response = CreateUserAPI.as_view()(request)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["user_name"], data["user_name"])
