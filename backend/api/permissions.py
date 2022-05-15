from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)


class IsStaffOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_staff
        )

class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return bool(
            # get access to superuser
            request.user.is_authenticated and request.user.is_superuser or
            # get acess to outhur of object
            obj.author == request.user
        )

class IsSuperuserOrStaffReadOnly(BasePermission):
    def has_permission(self, request, view):
        # if request.method in SAFE_METHODS and \
        #    request.user.is_staff and \
        #     request.user.is_authenticated:
        #     return True
        # return bool(
        #     request.user.is_superuser
        # )
        return bool(
            # get acess to outhur read only 
            request.method in SAFE_METHODS and request.user and request.user.is_staff or
            # get access to super user full
            request.user and request.user.is_superuser
        )