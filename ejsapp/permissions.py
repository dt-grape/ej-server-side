from rest_framework import permissions


class IsOwnerOnly(permissions.BasePermission):
    """
    Пользователь может редактировать или удалять объект только если он является его владельцем.
    """

    def has_object_permission(self, request, view, obj):
        # Проверяем, является ли текущий пользователь владельцем объекта
        return obj.owner == request.user
