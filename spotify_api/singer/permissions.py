from rest_framework.permissions import BasePermission

from spotify_api.singer.models import Singer


class IsSinger(BasePermission):
    """Allows access only to singers."""

    message = "You must be a singer to perform this action."

    def has_permission(self, request, view):
        try:
            return request.user.singer is not None
        except Singer.DoesNotExist:
            return False

class IsSingerOwner(BasePermission):
    """Allows access only to singers."""

    message = "You must be a singer to perform this action."

    def has_object_permission(self, request, view, obj):
        try:
            return request.user.singer == obj
        except Singer.DoesNotExist:
            return False

class IsSingerOrAdminUser(BasePermission):
    """
    Custom permission to allow singers and admin users to perform actions.
    """

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            try:
                return request.user.is_staff or request.user.singer
            except Singer.DoesNotExist:
                return False
        else:
            # For unauthenticated users, only allow "list" and "retrieve" actions
            return view.action in ["list", "retrieve"]