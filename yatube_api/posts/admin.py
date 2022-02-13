"""Импортируем модули с админкой и моделями."""
from django.contrib import admin

from .models import Comment, Follow, Group, Post


class PostAdmin(admin.ModelAdmin):
    """Создаем админку для модели постов и описываем поля."""

    list_display = (
        'pk',
        'text',
        'pub_date',
        'author',
        'group',
    )
    list_editable = ('group',)
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


class GroupAdmin(admin.ModelAdmin):
    """Создаем админку для модели групп и описываем поля."""

    list_display = (
        'title',
        'slug',
        'description',
    )
    search_fields = ('description',)
    list_filter = ('title',)
    empty_value_display = '-пусто-'


class CommentAdmin(admin.ModelAdmin):
    """Создаем админку для модели комментариев и описываем поля."""

    list_display = (
        'pk',
        'author',
        'text',
        'created',
    )
    search_fields = ('author', 'text',)
    list_filter = ('created',)
    empty_value_display = '-пусто-'


class FollowAdmin(admin.ModelAdmin):
    """Создаем админку для модели подписок и описываем поля."""

    list_display = (
        'pk',
        'user',
        'following'
    )
    search_fields = ('user', 'following')
    empty_value_display = '-пусто-'


admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Follow, FollowAdmin)
