import json
from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate
from rest_framework.authtoken.models import Token
from accounts.models.user import User
from accounts.models.wallet import Wallet
from accounts.api.wallet.edit_wallet import EditWalletAPI
from crypto.models.crypto import CryptoCurrency


class TestEditWalletAPI(TestCase):
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
        self.wallet = Wallet.objects.create(user=self.user, crypto_currency=self.crypto)
        self.token = Token.objects.get_or_create(user=self.user)

    def test_edit_wallet(self):
        factory = APIRequestFactory()
        data = {
            "amount": "10",
        }
        request = factory.put(
            f"/edit/{self.wallet.uuid}/",
            json.dumps(data),
            content_type="application/json",
        )
        force_authenticate(request, user=self.user, token=self.token)
        response = EditWalletAPI.as_view()(request, uuid=self.wallet.uuid)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(float(response.data["amount"]), float(data["amount"]))
