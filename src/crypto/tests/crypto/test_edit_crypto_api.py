import json
from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate
from rest_framework.authtoken.models import Token
from accounts.models.user import User
from crypto.models.crypto import CryptoCurrency
from crypto.api.crypto.edit_crypto import EditCryptoAPI


class TestEditCryptoAPI(TestCase):
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

    def test_edit_crypto(self):
        factory = APIRequestFactory()
        data = {
            "sale_price": "18",
        }
        request = factory.put(
            f"/edit/{self.crypto.abbreviation}/",
            json.dumps(data),
            content_type="application/json",
        )
        force_authenticate(request, user=self.user, token=self.token)
        response = EditCryptoAPI.as_view()(
            request, abbreviation=self.crypto.abbreviation
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(float(response.data["sale_price"]), float(data["sale_price"]))
