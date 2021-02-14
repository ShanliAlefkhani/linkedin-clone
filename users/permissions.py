from rest_framework import permissions, status
from rest_framework.response import Response


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.company.user == request.user


class IsPerson(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            person = request.user.person
            return bool(request.user and person)
        except:
            Response(status=status.HTTP_400_BAD_REQUEST)


class IsCompany(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            company = request.user.company
            return bool(request.user and company)
        except:
            Response(status=status.HTTP_400_BAD_REQUEST)
