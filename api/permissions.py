from rest_framework import permissions


class BookingPermission(permissions.BasePermission):
    """
    Permissions for any type of booking are as follow:
        - anyone can book (authenticated or not)
        - authenticate users can list elements, the view should take care of printing elements
          belonging to the user.
        - Retrieve, Update and Delete are reserved to owner or staff
    """
    def has_permission(self, request, view):
        if request.method in ['POST', 'OPTIONS']:
            return True

        if request.user and request.user.is_authenticated:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if obj.owner and obj.owner == request.user:
            return True

        if request.user.is_staff:
            return True
        else:
            return False


class IsAdminUserOrReadOnly(permissions.BasePermission):
    """
    Allows access only to admin users.
    """
    def has_permission(self, request, view):
        return bool(
            request.method in permissions.SAFE_METHODS or
            request.user and request.user.is_staff
        )
