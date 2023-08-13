from django.shortcuts import get_object_or_404
from accounts.models.user import User
from accounts.models.wallet import Wallet
from transactions.models import Transactions
from transactions.selectors import (
    calculate_crypto_price,
    is_user_balance_enough,
    buy_crypto_for_user,
)
from crypto.models.crypto import CryptoCurrency
from utils.exceptions import (
    InsufficientWalletBalance,
    InvalidUser,
)


def charge_wallet_func(
    user: User, user_name: str, crypto_currency: str, charge_amount: float
):
    if user.user_name != user_name:
        return InvalidUser
    crypto_currency = get_object_or_404(CryptoCurrency, abbreviation=crypto_currency)
    wallet = get_object_or_404(Wallet, user=user, crypto_currency=crypto_currency)
    before_amount = wallet.amount
    price_to_buy = calculate_crypto_price(crypto_currency, charge_amount)
    if is_user_balance_enough(user, price_to_buy):
        buy_crypto_for_user(
            user=user,
            wallet=wallet,
            crypto_amount=charge_amount,
            price=price_to_buy,
        )
        Transactions.objects.create(
            user=user,
            crypto_currency=crypto_currency,
            new_amount=charge_amount,
            before_amount=before_amount,
            note=f"increase {charge_amount} to {crypto_currency} wallet amount",
        )
        return user, wallet, crypto_currency
    return InsufficientWalletBalance
