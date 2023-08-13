from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate
from rest_framework.authtoken.models import Token
from accounts.models.user import User
from accounts.models.wallet import Wallet
from accounts.api.wallet.wallet_list import WalletListAPI
from crypto.models.crypto import CryptoCurrency


class TestWalletListAPI(TestCase):
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
        self.wallet = Wallet.objects.create(
            user=self.user,
            crypto_currency=self.crypto,
        )
        self.token = Token.objects.get_or_create(user=self.user)

    def test_list_wallet(self):
        factory = APIRequestFactory()
        request = factory.get("/")
        force_authenticate(request, user=self.user, token=self.token)
        response = WalletListAPI.as_view()(request)
        self.assertEqual(response.status_code, 200)
        wallet_count = Wallet.objects.count()
        self.assertEqual(len(response.data), wallet_count)
