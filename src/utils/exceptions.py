from rest_framework.exceptions import APIException
from rest_framework import status


class InvalidCryptoID(APIException):
    default_detail = "Invalid crypto id We cannot find any crypto with this id."
    status_code = status.HTTP_400_BAD_REQUEST


class InsufficientWalletBalance(APIException):
    default_detail = "Your wallet balance is insufficient."
    status_code = status.HTTP_400_BAD_REQUEST


class InvalidWallet(APIException):
    default_detail = "There is no wallet for this crypto or user"
    status_code = status.HTTP_400_BAD_REQUEST


class InvalidUser(APIException):
    default_detail = "You can only charge your own account."
    status_code = status.HTTP_400_BAD_REQUEST


class UserDoesNotExist(APIException):
    default_detail = "User doesn't exist"
    status_code = status.HTTP_404_NOT_FOUND
