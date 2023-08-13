from django.urls import path
from transactions.api.transactions.charge_user_amount import ChargeUserAmountAPI
from transactions.api.transactions.charge_wallet_amount import ChargeWalletAmountAPI
from transactions.api.transactions.transactions_list import TransactionsList

urlpatterns = [
    path("", TransactionsList.as_view(), name="Transactions-list"),
    path(
        "charge_user_amount/",
        ChargeUserAmountAPI.as_view(),
        name="charge_user_amount",
    ),
    path(
        "charge_wallet_amount/",
        ChargeWalletAmountAPI.as_view(),
        name="charge_wallet_amount",
    ),
]
