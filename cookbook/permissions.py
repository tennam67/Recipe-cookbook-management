from rest_framework.permissions import BasePermission


# object specific permission
class IsAuthorOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.author == request.user or request.user.is_superuser:
            return True

# general permission
# class IsUserReadOnly(BasePermission):
#     def has_permission(self, request, view):
#        if request.method == "GET":
#            return True
