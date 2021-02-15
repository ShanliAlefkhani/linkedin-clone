from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.company.user == request.user


class IsCompany(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            company = request.user.company
            return True
        except:
            return False
