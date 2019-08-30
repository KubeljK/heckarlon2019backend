from rest_framework import permissions


class IsLoggedInUserOrAdmin(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        return request.user and (obj == request.user or request.user.is_staff)

class IsDeveloperOrAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_staff or request.user.groups.filter(name='developers')

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or request.user.groups.filter(name='developers')

class OwnProfilePermission(permissions.BasePermission):
    """
    Object-level permission to only allow updating his own profile
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        # if request.method in permissions.SAFE_METHODS:
        #     return True

        return request.user.is_staff or obj == request.user
