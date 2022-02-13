"""Импортируем модули.

Метод получения объекта, фильтры, миксины,
ограничения, вьюсэты, пагинацию, сериалайзеры и моедли.
"""
from django.shortcuts import get_object_or_404
from rest_framework import filters, mixins, permissions, viewsets
from rest_framework.pagination import LimitOffsetPagination

from api.permissions import IsAuthorOrReadOnly
from api.serializers import (CommentSerializer, FollowSerializer,
                             GroupSerializer, PostSerializer)
from posts.models import Group, Post, User


class CreateListViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    """Создаем кастомный вьюсэт из миксинов для модели подписок."""

    pass


class CommentViewSet(viewsets.ModelViewSet):
    """Описываем набор представлений для модели комментариев."""

    serializer_class = CommentSerializer
    lookup_url_kwarg = 'comment_id'
    permission_classes = [IsAuthorOrReadOnly]

    def get_queryset(self):
        """Итерация выборки объектов для модели комментариев.

        Из строки запроса получаем id поста, получаем пост по его id и передаем
        в выборку все комментарии под этим постом.
        """
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        return post.comments.all()

    def perform_create(self, serializer):
        """Добавлем автора комментария в поле автор при создании коммента.

        Из строки запроса получаем id поста, получаем пост по его id и передаем
        в сериализатор в соответсвующие поля автора и пост.
        """
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        serializer.save(author=self.request.user, post=post)


class PostViewSet(viewsets.ModelViewSet):
    """Описываем набор представлений для модели постов."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_url_kwarg = 'post_id'
    permission_classes = [IsAuthorOrReadOnly]
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        """Добавлем автора поста в поле автор при создании поста.

        Из запроса получаем пользователя и передаем в сериализатор в поле
        автора пользователя, сделавшего POST запрос.
        """
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Описываем набор представлений для модели групп."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthorOrReadOnly]


class FollowViewSet(CreateListViewSet):
    """Описываем набор представлений для модели подписок."""

    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        """Итерация выборки объектов для модели подписок.

        Из запроса получаем id пользователя, получаем из модели пользовтелей
        пользователя по его id и передаем в выборку всех на кого подписан этот
        пользовтель.
        """
        user_id = self.request.user.id
        user = get_object_or_404(User, id=user_id)
        return user.follower.all()

    def perform_create(self, serializer):
        """Добавлем пользователя в поле при подписке на другого пользователя.

        Из запроса получаем id пользователя, получаем из модели пользовтелей
        пользователя по его id и передаем в сериализатор в соответствующее поле
        пользователя, сделавшего POST запрос.
        """
        user_id = self.request.user.id
        user = get_object_or_404(User, id=user_id)
        serializer.save(user=user)
