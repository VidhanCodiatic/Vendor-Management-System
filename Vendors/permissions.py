
from rest_framework import permissions

class UserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        # for superuser only
        elif request.user.is_superuser == True:
            return True

        return False
    
