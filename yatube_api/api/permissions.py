"""Импортируем модуль с ограничениями."""
from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Создаем кастомное ограничение."""

    def has_permission(self, request, view):
        """Ограничение на уровне запроса.

        Если безопасный метод запроса или пользователь авторизован.
        """
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        """Ограничение на уровне объекта.

        Если безопасный метод запроса или автор запроса является владельцем
        объекта или админом
        """
        return (request.user.is_superuser
                or request.method in permissions.SAFE_METHODS
                or obj.author == request.user)
