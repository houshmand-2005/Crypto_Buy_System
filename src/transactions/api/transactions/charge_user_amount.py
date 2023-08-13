from rest_framework import serializers
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
from transactions.managers import ChargeUserAmountManager


class ChargeUserAmountAPI(APIView):
    """API to Charge user Amount"""

    permission_classes = [IsAuthenticated]

    class ChargeUserAmountSerializer(serializers.Serializer):
        """
        **Output adn Input serializer for Charge User Amount**
        """

        user_name = serializers.CharField(max_length=30)
        charge_amount = serializers.DecimalField(
            max_digits=20, decimal_places=5, default=0
        )

    @extend_schema(
        tags=["Transactions"],
        request=ChargeUserAmountSerializer,
        responses=ChargeUserAmountSerializer,
    )
    def post(self, request) -> Response:
        """Create a new transactions for charge user amount"""
        serializer = self.ChargeUserAmountSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            user = request.user
            c_u_a = ChargeUserAmountManager()
            data = c_u_a.charge_user_amount(user=user, **data)
            response_data = {
                "user_name": user.user_name,
                "amount": data.amount,
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
