from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
from accounts.models.user import User
from utils.is_admin import IsAdminUser
from accounts.managers.user_manager import UserManager


class DeleteUserAPI(APIView):
    """API to delete user"""

    permission_classes = [IsAuthenticated, IsAdminUser]

    @extend_schema(tags=["User"], responses={status.HTTP_204_NO_CONTENT: None})
    def delete(self, request, user_name) -> Response:
        """Delete a user"""
        user_manager = UserManager()
        user_manager.delete_user(User, user_name)
        return Response(status=status.HTTP_204_NO_CONTENT)
