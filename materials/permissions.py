from rest_framework.permissions import BasePermission


class IsModerator(BasePermission):
    ''' Являетсяли user модератором '''

    def has_permission(self, request, view):
        if request.user.groups.filter(name='Модератор').exists():
            if request.method in ('GET', 'PATCH',):
                return True
            elif request.method in ('POST', 'DELETE',):
                return False
        return False


class IsOwner(BasePermission):
    ''' Являетсяли user создателем obj '''

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return True
            # return request.method in ['GET', 'PUT', 'PATCH', 'DELETE']
        return False
