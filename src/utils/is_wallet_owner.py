from rest_framework import permissions


class IsWalletOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check if the authenticated user is the owner of the wallet
        return obj.user == request.user
