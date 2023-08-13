from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate
from rest_framework.authtoken.models import Token
from accounts.models.user import User
from accounts.api.user.delete_user import DeleteUserAPI


class TestDeleteUserAPI(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            user_name="newuser",
            password="newpassword1234",
            phone_number="+989018924315",
            is_staff=True,
            is_superuser=True,
        )
        self.token = Token.objects.get_or_create(user=self.user)

    def test_delete_user(self):
        factory = APIRequestFactory()
        request = factory.delete(f"/delete/{self.user.user_name}/")
        force_authenticate(request, user=self.user, token=self.token)
        response = DeleteUserAPI.as_view()(request, user_name=self.user.user_name)
        self.assertEqual(response.status_code, 204)
