"""Импортируем модули с моделями, сериалайзерами и валидатором."""
from posts.models import Comment, Follow, Group, Post, User
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator


class CommentSerializer(serializers.ModelSerializer):
    """Создаем сериалайзер для модели комментариев."""

    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        """Создаем метакласс для полей модели комментариев."""

        fields = ('id', 'author', 'text', 'created', 'post')
        model = Comment
        read_only_fields = ('id', 'author', 'created', 'post')


class PostSerializer(serializers.ModelSerializer):
    """Создаем сериалайзер для модели постов."""

    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )
    comments = CommentSerializer(required=False, many=True)
    group = serializers.SlugRelatedField(
        slug_field='id',
        queryset=Group.objects.all(),
        required=False
    )

    class Meta:
        """Создаем метакласс для полей модели постов."""

        fields = ('id', 'text', 'author', 'image', 'group', 'pub_date',
                  'comments')
        model = Post
        read_only_fields = ('id', 'image', 'group', 'pub_date', 'comments')


class GroupSerializer(serializers.ModelSerializer):
    """Создаем сериалайзер для модели групп."""

    class Meta:
        """Создаем метакласс для полей модели групп."""

        fields = ('id', 'title', 'slug', 'description')
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    """Создаем сериалайзер для модели подписок."""

    user = serializers.SlugRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault(),
        slug_field='username'
    )
    following = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username'
    )

    class Meta:
        """Создаем метакласс для полей модели подписок и валидатора."""

        fields = ('user', 'following')
        model = Follow
        validator = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=['user', 'following']
            )
        ]

    def validate(self, data):
        """Кастомная валидация.

        Если безопасный подписка на самого себя или повторная на пользователя,
        на которого уже есть подписка, вызываем ошибку.
        """
        user = self.context['request'].user
        follow = data['following']
        if follow == user:
            raise serializers.ValidationError(
                'Запрещено подписываться на самого себя'
            )
        elif Follow.objects.filter(user=user, following=follow).exists():
            raise serializers.ValidationError(
                'Вы уже подписаны на данного пользователя'
            )
        return data
