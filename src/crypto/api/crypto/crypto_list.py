from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from crypto.models.crypto import CryptoCurrency


class CryptosListAPI(APIView):
    """API to receiving list of all sellable cryptos"""

    class CryptosListOutputSerializer(serializers.ModelSerializer):
        """
        **Output serializer for cryptos list API.**
        """

        class Meta:
            model = CryptoCurrency
            fields = "__all__"

    @extend_schema(tags=["Crypto"], responses=CryptosListOutputSerializer)
    def get(self, request) -> Response:
        """listing all cryptocurrencies"""
        cryptos = CryptoCurrency.objects.all()
        serializer = self.CryptosListOutputSerializer(
            instance=cryptos,
            many=True,
            context={"request": request},
        )
        return Response(serializer.data)
