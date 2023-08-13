from rest_framework import serializers
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
from crypto.models.crypto import CryptoCurrency
from crypto.managers import CryptoManager
from utils.is_admin import IsAdminUser


class CreateCryptosAPI(APIView):
    """API to create user"""

    permission_classes = [IsAuthenticated, IsAdminUser]

    class CryptosCreateInputAndOutputSerializer(serializers.ModelSerializer):
        """
        **Output adn Input serializer for cryptos list API**
        """

        class Meta:
            model = CryptoCurrency
            fields = "__all__"

    @extend_schema(
        tags=["Crypto"],
        request=CryptosCreateInputAndOutputSerializer,
        responses=CryptosCreateInputAndOutputSerializer,
    )
    def post(self, request) -> Response:
        """Create a new crypto currency"""
        serializer = self.CryptosCreateInputAndOutputSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            CryptoManager().create_crypto(**data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
