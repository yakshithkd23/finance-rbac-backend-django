from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    """
    Only Admin can perform write operations
    """
    def has_permission(self, request, view):
        return request.user.role == 'admin'


# class IsAnalystOrAdmin(BasePermission):
#     """
#     Analyst and Admin can read data
#     """
#     def has_permission(self, request, view):
#         return request.user.role in ['analyst', 'admin']
from rest_framework.permissions import BasePermission

class IsAnalystOrAdmin(BasePermission):
    def has_permission(self, request, view):
        #  Handle unauthenticated users
        if not request.user or not request.user.is_authenticated:
            return False

        #  Safe role check
        return request.user.role in ['analyst', 'admin']