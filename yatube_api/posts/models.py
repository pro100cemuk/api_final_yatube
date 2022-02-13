"""Импортируем метод получения модели пользователей и модуль моделей."""
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    """Создаем модель для групп и описываем поля."""

    title = models.CharField(max_length=200)
    slug = models.SlugField(
        max_length=200,
        unique=True,
        db_index=True
    )
    description = models.TextField(blank=True)

    def __str__(self):
        """Метод получения строкового названия группы."""
        return self.title


class Post(models.Model):
    """Создаем модель для постов и описываем поля."""

    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name='posts',
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to='posts/',
        null=True,
        blank=True
    )

    def __str__(self):
        """Метод получения строкового значения текста поста."""
        return self.text


class Comment(models.Model):
    """Создаем модель для комментариев и описываем поля."""

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)

    class Meta:
        """Создаем метакласс для сортировки по дате создания комментариев."""

        ordering = ['-created']


class Follow(models.Model):
    """Создаем модель для подписок и описываем поля."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
    )

    class Meta:
        """Создаем метакласс для проверки уникальности взаимосвязи полей."""

        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'], name='unique_following'
            )
        ]
