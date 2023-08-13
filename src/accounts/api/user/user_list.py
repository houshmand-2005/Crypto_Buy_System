from typing import List
from rest_framework import serializers
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
from accounts.models.user import User
from accounts.models.wallet import Wallet
from utils.is_admin import IsAdminUser


class UserListAPI(APIView):
    """API to create user"""

    permission_classes = [IsAuthenticated, IsAdminUser]

    class WalletSerializer(serializers.ModelSerializer):
        """
        **Serializer for user wallets**
        """

        class Meta:
            model = Wallet
            fields = "__all__"

    class UserListOutputSerializer(serializers.ModelSerializer):
        """
        **Output serializer for user list API**
        """

        wallets = serializers.SerializerMethodField()

        class Meta:
            model = User
            fields = "__all__"

        def get_wallets(self, user) -> List[dict]:
            wallets = user.wallet.all()
            return UserListAPI.WalletSerializer(wallets, many=True).data

    @extend_schema(tags=["User"], responses=UserListOutputSerializer)
    def get(self, request) -> Response:
        """Listing all users"""
        users = User.objects.all()
        serializer = self.UserListOutputSerializer(
            instance=users,
            many=True,
            context={"request": request},
        )
        return Response(serializer.data)
