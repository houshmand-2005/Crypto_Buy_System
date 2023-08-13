import json
from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate
from rest_framework.authtoken.models import Token
from accounts.models.user import User
from crypto.api.crypto.create_crypto import CreateCryptosAPI


class TestCreateCryptoAPI(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            user_name="newuser",
            password="newpassword1234",
            phone_number="+989018924315",
            is_staff=True,
            is_superuser=True,
        )
        self.token = Token.objects.get_or_create(user=self.user)

    def test_create_crypto(self):
        factory = APIRequestFactory()
        data = {
            "abbreviation": "BTC",
            "name": "Bitcoin",
            "purchase_price": "10",
            "sale_price": "12",
        }
        request = factory.post(
            "/create/", json.dumps(data), content_type="application/json"
        )
        force_authenticate(request, user=self.user, token=self.token)
        response = CreateCryptosAPI.as_view()(request)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["abbreviation"], data["abbreviation"])
