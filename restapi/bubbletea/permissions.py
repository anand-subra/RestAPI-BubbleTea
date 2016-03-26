#Creation of custom permissions based on rest_framework's existing permissions class
from rest_framework import permissions

#Edits can only be made by object owners
#Otherwise, other users have read-only access
class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Read permissions granted if requests are of safe-methods types (GET, HEAD or OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permission granted if object owner is also current, logged-in user
        return obj.username == request.user
