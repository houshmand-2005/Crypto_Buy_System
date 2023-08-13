from typing import List
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
from accounts.models.user import User
from accounts.models.wallet import Wallet


class GetUserAPI(APIView):
    """API to create user"""

    permission_classes = [IsAuthenticated]

    class WalletSerializer(serializers.ModelSerializer):
        """
        **Serializer for user wallets**
        """

        class Meta:
            model = Wallet
            fields = "__all__"

    class GetUserOutputSerializer(serializers.ModelSerializer):
        """
        **Output serializer for user list API**
        """

        wallets = serializers.SerializerMethodField()

        class Meta:
            model = User
            fields = "__all__"

        def get_wallets(self, user) -> List[dict]:
            wallets = user.wallet.all()
            return GetUserAPI.WalletSerializer(wallets, many=True).data

    @extend_schema(
        tags=["User"], operation_id="get_user", responses=GetUserOutputSerializer
    )
    def get(self, request, user_name) -> Response:
        """Listing all users"""
        if request.user.user_name != user_name and not request.user.is_staff:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
            )
        user = get_object_or_404(User, user_name=user_name)
        serializer = self.GetUserOutputSerializer(
            instance=user,
            context={"request": request},
        )
        return Response(serializer.data, status=status.HTTP_200_OK)
