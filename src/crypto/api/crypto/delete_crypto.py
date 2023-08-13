from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
from utils.is_admin import IsAdminUser
from crypto.managers import CryptoManager
from crypto.models.crypto import CryptoCurrency


class DeleteCryptoAPI(APIView):
    """API to delete user"""

    permission_classes = [IsAuthenticated, IsAdminUser]

    @extend_schema(tags=["Crypto"], responses={status.HTTP_204_NO_CONTENT: None})
    def delete(self, request, abbreviation) -> Response:
        """Delete a user"""
        crypto_manager = CryptoManager()
        crypto_manager.delete_crypto(CryptoCurrency, abbreviation=abbreviation)
        return Response(status=status.HTTP_204_NO_CONTENT)
