from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
from accounts.models.wallet import Wallet
from utils.is_admin import IsAdminUser
from accounts.managers.wallet_manager import WalletManager


class DeleteWalletAPI(APIView):
    """API to delete user"""

    permission_classes = [IsAuthenticated, IsAdminUser]

    @extend_schema(tags=["Wallet"], responses={status.HTTP_204_NO_CONTENT: None})
    def delete(self, request, uuid) -> Response:
        """Delete a user"""
        wallet_manager = WalletManager()
        wallet_manager.delete_Wallet(Wallet, uuid=uuid)
        return Response(status=status.HTTP_204_NO_CONTENT)
