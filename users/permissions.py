from rest_framework.permissions import BasePermission


class IsUserProfile(BasePermission):
    ''' Являетсяли user - создателем '''

    def has_object_permission(self, request, view, obj):
        if request.user.email == obj.email:
            return True
        return False
