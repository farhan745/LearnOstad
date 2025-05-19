from rest_framework import permissions

class IsReviewerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read-only permissions are allowed for any request method in SAFE_METHODS (e.g., GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Write permissions are only allowed if the user is the reviewer
        return obj.reviewer == request.user