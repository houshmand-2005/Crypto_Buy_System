from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate
from rest_framework.authtoken.models import Token
from accounts.models.user import User
from accounts.models.wallet import Wallet
from accounts.api.wallet.delete_wallet import DeleteWalletAPI
from crypto.models.crypto import CryptoCurrency


class TestDeleteWalletAPI(TestCase):
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

    def test_delete_wallet(self):
        factory = APIRequestFactory()
        request = factory.delete(f"/delete/{self.wallet.uuid}")
        force_authenticate(request, user=self.user, token=self.token)
        response = DeleteWalletAPI.as_view()(request, uuid=self.wallet.uuid)
        self.assertEqual(response.status_code, 204)
