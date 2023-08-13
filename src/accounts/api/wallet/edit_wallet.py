from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
from accounts.models.wallet import Wallet
from accounts.managers.wallet_manager import WalletManager
from utils.is_admin import IsAdminUser


class EditWalletAPI(APIView):
    """API to update wallet"""

    permission_classes = [IsAuthenticated, IsAdminUser]

    class EditWalletInputAndOutputSerializer(serializers.Serializer):
        """
        **Output and Input serializer for updating wallet**
        """

        amount = serializers.DecimalField(max_digits=20, decimal_places=5)
        wallet_address = serializers.CharField(required=False)

    @extend_schema(
        tags=["Wallet"],
        request=EditWalletInputAndOutputSerializer,
        responses=EditWalletInputAndOutputSerializer,
    )
    def put(self, request, uuid) -> Response:
        """Update a Wallet"""
        try:
            wallet = get_object_or_404(Wallet, uuid=uuid)
        except ValidationError:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = self.EditWalletInputAndOutputSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            user_manager = WalletManager()
            user_manager.update_wallet(wallet, **data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
