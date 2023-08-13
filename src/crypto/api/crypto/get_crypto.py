from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from crypto.models.crypto import CryptoCurrency


class GetCryptoAPI(APIView):
    """API to create user"""

    class GetCryptoOutputSerializer(serializers.ModelSerializer):
        """
        **Output serializer for user list API**
        """

        class Meta:
            model = CryptoCurrency
            fields = "__all__"

    @extend_schema(
        tags=["Crypto"], operation_id="get_crypto", responses=GetCryptoOutputSerializer
    )
    def get(self, request, abbreviation) -> Response:
        """Listing all users"""
        crypto = get_object_or_404(CryptoCurrency, abbreviation=abbreviation)
        serializer = self.GetCryptoOutputSerializer(
            instance=crypto,
            context={"request": request},
        )
        return Response(serializer.data, status=status.HTTP_200_OK)
