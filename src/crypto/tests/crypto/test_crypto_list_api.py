from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate
from rest_framework.authtoken.models import Token
from accounts.models.user import User
from crypto.models.crypto import CryptoCurrency
from crypto.api.crypto.crypto_list import CryptosListAPI


class TestListCryptoAPI(TestCase):
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

    def test_list_crypto(self):
        factory = APIRequestFactory()
        request = factory.get("/")
        force_authenticate(request, user=self.user, token=self.token)
        response = CryptosListAPI.as_view()(request)
        self.assertEqual(response.status_code, 200)
        crypto_count = CryptoCurrency.objects.count()
        self.assertEqual(len(response.data), crypto_count)
