from rest_framework import permissions


class IsUserOrStaffUser(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):

        if request.user.is_staff:
            return True

        return obj == request.user
