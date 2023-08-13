from django.contrib.auth.password_validation import validate_password
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from accounts.models.user import User
from accounts.managers.user_manager import UserManager
from utils.validators import phone_validator, username_validator


class EditUserAPI(APIView):
    """API to update user"""

    class EditUserInputAndOutputSerializer(serializers.ModelSerializer):
        """
        **Output and Input serializer for updating a user**
        """

        class Meta:
            model = User
            fields = "__all__"

        user_name = serializers.CharField(
            required=False,
            validators=[username_validator],
        )
        phone_number = serializers.CharField(
            required=False,
            validators=[phone_validator],
        )
        password = serializers.CharField(
            required=False,
            validators=[validate_password],
        )
        last_login = serializers.DateTimeField(required=False)

    @extend_schema(
        tags=["User"],
        request=EditUserInputAndOutputSerializer,
        responses=EditUserInputAndOutputSerializer,
    )
    def put(self, request, user_name) -> Response:
        """Update a user"""
        if request.user.user_name != user_name and not request.user.is_staff:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
            )
        user = get_object_or_404(User, user_name=user_name)
        serializer = self.EditUserInputAndOutputSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            user_manager = UserManager()
            user_manager.update_user(user, **data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
