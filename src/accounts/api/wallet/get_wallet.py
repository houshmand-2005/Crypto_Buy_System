from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from rest_framework import serializers
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
from accounts.models.wallet import Wallet


class GetWalletAPI(APIView):
    """API to create user"""

    permission_classes = [IsAuthenticated]

    class GetWalletOutputSerializer(serializers.ModelSerializer):
        """
        **Output serializer for user list API**
        """

        class Meta:
            model = Wallet
            fields = "__all__"

    @extend_schema(
        tags=["Wallet"], operation_id="get_wallet", responses=GetWalletOutputSerializer
    )
    def get(self, request, uuid) -> Response:
        """Listing all users"""
        try:
            wallet = get_object_or_404(Wallet, uuid=uuid)
        except ValidationError:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = self.GetWalletOutputSerializer(
            instance=wallet,
            context={"request": request},
        )
        return Response(serializer.data, status=status.HTTP_200_OK)
