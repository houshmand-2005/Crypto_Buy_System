from django.db import models
from django.shortcuts import get_object_or_404
from crypto.models.crypto import CryptoCurrency


class CryptoManager(models.Manager):
    def create_crypto(
        self,
        abbreviation: str,
        name: str,
        purchase_price: float,
        sale_price: float,
        logo: models.ImageField = "",
    ) -> "CryptoCurrency":
        crypto = CryptoCurrency.objects.create(
            abbreviation=abbreviation,
            name=name,
            purchase_price=purchase_price,
            sale_price=sale_price,
            logo=logo,
        )
        return crypto

    def delete_crypto(self, crypto, abbreviation):
        crypto = get_object_or_404(crypto, abbreviation=abbreviation)
        crypto.delete()

    def update_wallet(self, crypto, **data):
        for key, value in data.items():
            setattr(crypto, key, value)
        crypto.save()
