
from rest_framework import permissions

    
class VendorPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_active == True:
            return True
        # for superuser only
        elif request.user.is_superuser == True:
            return True

        return False
    
