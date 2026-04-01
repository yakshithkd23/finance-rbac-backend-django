from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    """
    Only Admin can perform write operations
    """
    def has_permission(self, request, view):
        return request.user.role == 'admin'


class IsAnalystOrAdmin(BasePermission):
    """
    Analyst and Admin can read data
    """
    def has_permission(self, request, view):
        return request.user.role in ['analyst', 'admin']