from rest_framework import serializers
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
from transactions.managers import ChargeWalletAmountManager


class ChargeWalletAmountAPI(APIView):
    """API to create user"""

    permission_classes = [IsAuthenticated]

    class ChargeWalletAmountSerializer(serializers.Serializer):
        """
        **Output adn Input serializer for Charge User Amount**
        """

        user_name = serializers.CharField(max_length=30)
        crypto_currency = serializers.CharField(max_length=3)
        charge_amount = serializers.DecimalField(
            max_digits=20, decimal_places=5, default=0
        )

    @extend_schema(
        tags=["Transactions"],
        request=ChargeWalletAmountSerializer,
        responses=ChargeWalletAmountSerializer,
    )
    def post(self, request) -> Response:
        """Create a new crypto currency"""
        serializer = self.ChargeWalletAmountSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            user = request.user
            c_w_a = ChargeWalletAmountManager()
            data = c_w_a.charge_wallet_amount(user=user, **data)
            response_data = {
                "user_name": data[0].user_name,
                "user_amount": data[0].amount,
                "crypto_currency": data[2].name,
                "wallet_amount": data[1].amount,
                "wallet_address": data[1].wallet_address,
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
