from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from transactions.models.transaction import Transactions


class TransactionsList(APIView):
    """API to receiving list of all Transactions"""

    class TransactionsListOutputSerializer(serializers.ModelSerializer):
        """
        **Output serializer for Transactions list API**
        """

        class Meta:
            model = Transactions
            fields = "__all__"

    @extend_schema(tags=["Transactions"], responses=TransactionsListOutputSerializer)
    def get(self, request) -> Response:
        """listing all cryptocurrencies"""
        transactions = Transactions.objects.all()
        serializer = self.TransactionsListOutputSerializer(
            instance=transactions,
            many=True,
            context={"request": request},
        )
        return Response(serializer.data)
