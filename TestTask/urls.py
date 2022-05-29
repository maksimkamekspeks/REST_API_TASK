from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from api import views
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', views.UserViewSet)
router.register(r'posts', views.PostViewSet)
router.register(r'likes', views.LikesViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('register/', views.UserCreateViewSet.as_view()),

    path('<int:post_id>/like', views.like, name='like'),
    path('analitics/<str:date_interval>', views.likes_by_date)
]

