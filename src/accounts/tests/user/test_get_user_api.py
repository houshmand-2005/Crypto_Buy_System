from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate
from rest_framework.authtoken.models import Token
from accounts.models.user import User
from accounts.api.user.get_user import GetUserAPI


class TestGetUserAPI(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            user_name="newuser",
            password="newpassword1234",
            phone_number="+989018924315",
        )
        self.token = Token.objects.get_or_create(user=self.user)

    def test_get_user_authenticated(self):
        factory = APIRequestFactory()
        request = factory.get(f"/{self.user.user_name}/")
        force_authenticate(request, user=self.user, token=self.token)
        response = GetUserAPI.as_view()(request, user_name=self.user.user_name)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["user_name"], self.user.user_name)

    def test_get_user_unauthenticated(self):
        factory = APIRequestFactory()
        request = factory.get(f"/users/{self.user.user_name}/")
        response = GetUserAPI.as_view()(request, user_name=self.user.user_name)
        self.assertEqual(response.status_code, 401)
