from django.db import models
from accounts.models.user import User
from transactions.models import Transactions
from utils.exceptions import InvalidUser
from transactions.charge_wallet import charge_wallet_func


class ChargeUserAmountManager(models.Manager):
    def charge_user_amount(
        self, user: User, user_name: str, charge_amount: float
    ) -> User:
        before_amount = user.amount
        if user.user_name != user_name:
            return InvalidUser
        user.charge_wallet(amount=charge_amount)
        Transactions.objects.create(
            user=user,
            new_amount=user.amount,
            before_amount=before_amount,
            note=f"increase {charge_amount} to user amount",
        )
        return user


class ChargeWalletAmountManager(models.Manager):
    def charge_wallet_amount(
        self, user: User, user_name: str, crypto_currency: str, charge_amount: float
    ) -> User:
        return charge_wallet_func(user, user_name, crypto_currency, charge_amount)
