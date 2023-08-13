from django.urls import path
from crypto.api.crypto.crypto_list import CryptosListAPI
from crypto.api.crypto.create_crypto import CreateCryptosAPI
from crypto.api.crypto.delete_crypto import DeleteCryptoAPI
from crypto.api.crypto.get_crypto import GetCryptoAPI
from crypto.api.crypto.edit_crypto import EditCryptoAPI

urlpatterns = [
    path("", CryptosListAPI.as_view(), name="cryptos-list"),
    path("create/", CreateCryptosAPI.as_view(), name="create_crypto"),
    path("<str:abbreviation>", GetCryptoAPI.as_view(), name="get_crypto"),
    path("delete/<str:abbreviation>", DeleteCryptoAPI.as_view(), name="delete_crypto"),
    path("edit/<str:abbreviation>", EditCryptoAPI.as_view(), name="edit_crypto"),
]
