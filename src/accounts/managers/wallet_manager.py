from django.db import models
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from accounts.models.wallet import Wallet
from accounts.models.user import User
from crypto.models.crypto import CryptoCurrency


class WalletManager(models.Manager):
    def create_wallet(
        self,
        user_name: str,
        crypto_currency: str,
    ) -> "Wallet":
        """create raw wallet for user"""
        user = get_object_or_404(User, user_name=user_name)
        crypto_currency = get_object_or_404(
            CryptoCurrency, abbreviation=crypto_currency
        )
        if Wallet.objects.filter(user=user, crypto_currency=crypto_currency).exists():
            raise serializers.ValidationError(
                "Wallet already exists for this user and crypto currency"
            )
        crypto = Wallet.objects.create(user=user, crypto_currency=crypto_currency)
        return crypto

    def delete_Wallet(self, wallet, uuid):
        wallet = get_object_or_404(wallet, uuid=uuid)
        wallet.delete()

    def update_wallet(self, wallet, **data):
        for key, value in data.items():
            setattr(wallet, key, value)
        wallet.save()
