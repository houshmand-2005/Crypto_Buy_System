from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
from crypto.models.crypto import CryptoCurrency
from crypto.managers import CryptoManager
from utils.is_admin import IsAdminUser


class EditCryptoAPI(APIView):
    """API to update wallet"""

    permission_classes = [IsAuthenticated, IsAdminUser]

    class EditCryptoInputAndOutputSerializer(serializers.ModelSerializer):
        """
        **Output and Input serializer for updating wallet**
        """

        class Meta:
            model = CryptoCurrency
            fields = "__all__"

        abbreviation = serializers.CharField(required=False)
        name = serializers.CharField(required=False)
        purchase_price = serializers.DecimalField(
            required=False,
            max_digits=20,
            decimal_places=5,
        )
        sale_price = serializers.DecimalField(
            required=False,
            max_digits=20,
            decimal_places=5,
        )
        logo = serializers.ImageField(
            required=False,
        )

    @extend_schema(
        tags=["Crypto"],
        request=EditCryptoInputAndOutputSerializer,
        responses=EditCryptoInputAndOutputSerializer,
    )
    def put(self, request, abbreviation) -> Response:
        """Update a Wallet"""
        try:
            crypto_currency = get_object_or_404(
                CryptoCurrency, abbreviation=abbreviation
            )
        except ValidationError:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = self.EditCryptoInputAndOutputSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            user_manager = CryptoManager()
            user_manager.update_wallet(crypto_currency, **data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
