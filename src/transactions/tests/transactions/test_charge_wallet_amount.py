import json
from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate
from rest_framework.authtoken.models import Token
from accounts.models.user import User
from accounts.models.wallet import Wallet
from crypto.models.crypto import CryptoCurrency
from transactions.api.transactions.charge_wallet_amount import ChargeWalletAmountAPI


class TestChargeWalletAmountAPI(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            user_name="newuser",
            password="newpassword1234",
            phone_number="+989018924315",
            amount=10,
            is_staff=True,
            is_superuser=True,
        )
        self.crypto = CryptoCurrency.objects.create(
            abbreviation="BTC",
            name="Bitcoin",
            purchase_price=2,
        )
        self.wallet = Wallet.objects.create(user=self.user, crypto_currency=self.crypto)
        self.token = Token.objects.get_or_create(user=self.user)

    def test_charge_wallet_amount(self):
        factory = APIRequestFactory()
        data = {
            "user_name": "newuser",
            "charge_amount": "3",
            "crypto_currency": "BTC",
        }
        request = factory.post(
            "/charge_wallet_amount/", json.dumps(data), content_type="application/json"
        )
        force_authenticate(request, user=self.user, token=self.token)
        response = ChargeWalletAmountAPI.as_view()(request)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            float(response.data["wallet_amount"]), float(data["charge_amount"])
        )
