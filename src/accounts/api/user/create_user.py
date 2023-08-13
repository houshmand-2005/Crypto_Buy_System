from rest_framework import serializers
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
from accounts.models.user import User
from accounts.managers.user_manager import UserManager
from utils.is_admin import IsAdminUser


class CreateUserAPI(APIView):
    """API to create user"""

    # permission_classes = [IsAuthenticated, IsAdminUser]

    class UserListInputAndOutputSerializer(serializers.ModelSerializer):
        """
        **Output and Input serializer for creating a new user currency**
        """

        class Meta:
            model = User
            fields = "__all__"

    @extend_schema(
        tags=["User"],
        request=UserListInputAndOutputSerializer,
        responses=UserListInputAndOutputSerializer,
    )
    def post(self, request) -> Response:
        """Create a new user"""
        serializer = self.UserListInputAndOutputSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            user_manager = UserManager()
            user_manager.create_user(**data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
