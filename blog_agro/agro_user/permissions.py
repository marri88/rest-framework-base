from rest_framework.permissions import BasePermission, AllowAny
from rest_framework.exceptions import PermissionDenied

class IsClient(BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        try:
            request.user.is_client
        except:
            raise PermissionDenied('У вас нету прав доступа')
        return bool(request.user and request.user.is_client)
