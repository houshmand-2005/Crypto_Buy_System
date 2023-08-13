import json
from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate
from rest_framework.authtoken.models import Token
from accounts.models.user import User
from crypto.models.crypto import CryptoCurrency
from transactions.api.transactions.charge_user_amount import ChargeUserAmountAPI


class TestChargeUserAmountAPI(TestCase):
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

    def test_charge_user_amount(self):
        factory = APIRequestFactory()
        data = {
            "user_name": "newuser",
            "charge_amount": "20",
        }
        request = factory.post(
            "/charge_user_amount/", json.dumps(data), content_type="application/json"
        )
        force_authenticate(request, user=self.user, token=self.token)
        response = ChargeUserAmountAPI.as_view()(request)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(float(response.data["amount"]), float(data["charge_amount"]))
