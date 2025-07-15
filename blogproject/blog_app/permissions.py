from rest_framework import permissions

class IsWriterOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow safe methods for all
        if request.method in permissions.SAFE_METHODS:
            return True
        # Only allow writers to POST, PUT, PATCH, DELETE
        return request.user.is_authenticated and getattr(request.user, 'role', None) == 'writer'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Only allow writers to modify their own posts
        return obj.author == request.user and request.user.role == 'writer'
