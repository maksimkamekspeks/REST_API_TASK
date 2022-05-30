from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from api.views import PostViewSet, LikesList
from users.views import UserViewSet, UserCreateViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('register/', UserCreateViewSet.as_view()),
    path('likes/', LikesList.as_view()),
]

