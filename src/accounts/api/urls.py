from django.urls import path, include
from accounts.api.user.create_user import CreateUserAPI
from accounts.api.user.delete_user import DeleteUserAPI
from accounts.api.user.edit_user import EditUserAPI
from accounts.api.user.user_list import UserListAPI
from accounts.api.user.get_user import GetUserAPI
from accounts.api.wallet.wallet_list import WalletListAPI
from accounts.api.wallet.create_wallet import CreateWalletAPI
from accounts.api.wallet.delete_wallet import DeleteWalletAPI
from accounts.api.wallet.edit_wallet import EditWalletAPI
from accounts.api.wallet.get_wallet import GetWalletAPI

users_urlpatterns = [
    path("", UserListAPI.as_view(), name="users-list"),
    path("<str:user_name>", GetUserAPI.as_view(), name="get_user"),
    path("create/", CreateUserAPI.as_view(), name="create_user"),
    path("delete/<str:user_name>", DeleteUserAPI.as_view(), name="delete_user"),
    path("edit/<str:user_name>", EditUserAPI.as_view(), name="edit_user"),
]

wallets_urlpatterns = [
    path("", WalletListAPI.as_view(), name="wallets-list"),
    path("<str:uuid>", GetWalletAPI.as_view(), name="get_wallet"),
    path("create/", CreateWalletAPI.as_view(), name="create_wallet"),
    path("delete/<str:uuid>", DeleteWalletAPI.as_view(), name="delete_wallet"),
    path("edit/<str:uuid>", EditWalletAPI.as_view(), name="edit_wallet"),
]

urlpatterns = [
    path("users/", include(users_urlpatterns)),
    path("wallets/", include(wallets_urlpatterns)),
]
