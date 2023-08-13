import json
from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate
from rest_framework.authtoken.models import Token
from accounts.models.user import User
from accounts.api.wallet.create_wallet import CreateWalletAPI
from crypto.models.crypto import CryptoCurrency


class TestCreateWalletAPI(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            user_name="newuser",
            password="newpassword1234",
            phone_number="+989018924315",
            is_staff=True,
            is_superuser=True,
        )
        self.crypto = CryptoCurrency.objects.create(
            abbreviation="BTC",
            name="Bitcoin",
        )
        self.token = Token.objects.get_or_create(user=self.user)

    def test_create_wallet(self):
        factory = APIRequestFactory()
        data = {"user_name": "newuser", "crypto_currency": self.crypto.abbreviation}
        request = factory.post(
            "/create/", json.dumps(data), content_type="application/json"
        )
        force_authenticate(request, user=self.user, token=self.token)
        response = CreateWalletAPI.as_view()(request)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["crypto_currency"], self.crypto.abbreviation)
