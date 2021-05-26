from rest_framework.permissions import BasePermission, SAFE_METHODS


class isAdminUserOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # if method is GET return true
        if request.method in SAFE_METHODS:
            return True

        return request.user.is_superuser
