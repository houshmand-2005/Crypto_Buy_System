from crypto.models.crypto import CryptoCurrency
from utils.exceptions import InvalidCryptoID
from accounts.models.user import User
from accounts.models.wallet import Wallet
from transactions.models import Transactions


def calculate_crypto_price(crypto: CryptoCurrency, amount: float) -> int | float:
    """
    calculating how much user must pay for this crypto.

    crypto_name : name of cryptos user wants to buy
    amount : how much user want buy from this crypto

    return : calculate price
    """
    if crypto:
        return crypto.purchase_price * amount
    raise InvalidCryptoID


def is_user_balance_enough(user: User, amount_to_buy: int | float) -> bool:
    """user have enough money"""
    return user.amount >= amount_to_buy


def buy_crypto_for_user(
    user: User,
    wallet: Wallet,
    crypto_amount: float,
    price: float,
) -> None:
    before_amount = user.amount
    user.decreasing_wallet(price)
    Transactions.objects.create(
        user=user,
        new_amount=user.amount,
        before_amount=before_amount,
        note=f"decrease {price} to user amount",
    )
    wallet.charge_wallet(crypto_amount)
