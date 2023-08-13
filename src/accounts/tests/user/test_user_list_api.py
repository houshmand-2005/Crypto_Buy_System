from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate
from rest_framework.authtoken.models import Token
from accounts.models.user import User
from accounts.api.user.user_list import UserListAPI


class TestUserListAPI(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user_with_permission = User.objects.create(
            user_name="user_with_permission",
            password="password1234",
            phone_number="+989012345678",
            is_staff=True,
            is_superuser=True,
        )
        self.token_with_permission = Token.objects.create(
            user=self.user_with_permission
        )

        self.user_without_permission = User.objects.create(
            user_name="user_without_permission",
            password="password1234",
            phone_number="+989076543210",
            is_staff=False,
            is_superuser=False,
        )
        self.token_without_permission = Token.objects.create(
            user=self.user_without_permission
        )

    def test_list_users_with_permission(self):
        request = self.factory.get("/")
        force_authenticate(
            request,
            user=self.user_with_permission,
            token=self.token_with_permission,
        )
        response = UserListAPI.as_view()(request)
        self.assertEqual(response.status_code, 200)
        user_count = User.objects.count()
        self.assertEqual(len(response.data), user_count)

    def test_list_users_without_permission(self):
        request = self.factory.get("/users/")
        force_authenticate(
            request,
            user=self.user_without_permission,
            token=self.token_without_permission,
        )
        response = UserListAPI.as_view()(request)
        self.assertEqual(response.status_code, 403)
