from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from accounts.models.wallet import Wallet
from utils.is_admin import IsAdminUser


class WalletListAPI(APIView):
    """API to receiving list of all wallets"""

    permission_classes = [IsAuthenticated, IsAdminUser]

    class WalletListOutputSerializer(serializers.ModelSerializer):
        """
        **Output serializer for wallet list API**
        """

        class Meta:
            model = Wallet
            fields = "__all__"

    @extend_schema(tags=["Wallet"], responses=WalletListOutputSerializer)
    def get(self, request) -> Response:
        """listing all wallets"""
        wallets = Wallet.objects.all()
        serializer = self.WalletListOutputSerializer(
            instance=wallets,
            many=True,
            context={"request": request},
        )
        return Response(serializer.data)
