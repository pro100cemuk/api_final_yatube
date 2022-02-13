"""Импортируем модули для маршрутизации адресов, роутер и вьюсэты."""
from django.urls import include, path
from rest_framework.routers import SimpleRouter

from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

v1_router = SimpleRouter()
v1_router.register('posts', PostViewSet)
v1_router.register('groups', GroupViewSet)
v1_router.register(r'posts/(?P<post_id>\d+)/comments',
                   CommentViewSet, basename='comments')
v1_router.register('follow', FollowViewSet, basename='follow')

"""По заданию создание пользователей не требуется(закоменченная строка) """


urlpatterns = [
    # path('v1/auth/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(v1_router.urls)),
]
