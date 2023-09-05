from rest_framework.permissions import BasePermission, SAFE_METHODS

from spotify_api.singer.models import Singer


class IsSinger(BasePermission):
    """Allows access only to singers."""

    message = "You must be a singer to perform this action."

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            try:
                return request.user.singer
            except Singer.DoesNotExist:
                return False
        else:
            return view.action in ["list", "retrieve"]

class IsSingerOwner(BasePermission):
    """Allows access only to singers."""

    message = "You must be a singer to perform this action."

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            try:
                return request.user.singer == obj
            except Singer.DoesNotExist:
                return False
        else:
            return view.action == "retrieve"
