import json
from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate
from rest_framework.authtoken.models import Token
from accounts.models.user import User
from accounts.api.user.edit_user import EditUserAPI


class TestEditUserAPI(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            user_name="newuser",
            password="newpassword1234",
            phone_number="+989018924315",
        )
        self.token = Token.objects.get_or_create(user=self.user)

    def test_edit_user(self):
        factory = APIRequestFactory()
        data = {
            "phone_number": "+989012345678",
        }
        request = factory.put(
            f"/edit/{self.user.user_name}/",
            json.dumps(data),
            content_type="application/json",
        )
        force_authenticate(request, user=self.user, token=self.token)
        response = EditUserAPI.as_view()(request, user_name=self.user.user_name)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["phone_number"], data["phone_number"])
