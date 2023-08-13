from rest_framework import serializers
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
from accounts.managers.wallet_manager import WalletManager
from utils.is_admin import IsAdminUser


class CreateWalletAPI(APIView):
    """API to wallet user"""

    permission_classes = [IsAuthenticated, IsAdminUser]

    class WalletCreateInputAndOutputSerializer(serializers.Serializer):
        """
        **Output and Input serializer for creating a new wallet**
        """

        user_name = serializers.CharField(max_length=30)
        crypto_currency = serializers.CharField(max_length=3)

    @extend_schema(
        tags=["Wallet"],
        request=WalletCreateInputAndOutputSerializer,
        responses=WalletCreateInputAndOutputSerializer,
    )
    def post(self, request) -> Response:
        """Create a new wallet"""
        serializer = self.WalletCreateInputAndOutputSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            wallet_manager = WalletManager()
            crypto = wallet_manager.create_wallet(**data)
            wallet_info = {
                "user_name": data["user_name"],
                "crypto_currency": data["crypto_currency"],
                "wallet_address": crypto.wallet_address,
            }
            return Response(wallet_info, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
