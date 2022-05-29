from django.contrib.auth.models import User
from api.models import Post, Likes
from api.serializers import UserSerializer, PostSerializer, LikesSerializer, UserCreateSerializer
from api.permissions import IsOwnerOrReadOnly
from rest_framework import permissions, viewsets
from rest_framework import mixins
from rest_framework import generics
from api.services import add_remove_like, aggregated_likes_by_date
from django.http import HttpResponse, HttpResponseRedirect




class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UserCreateViewSet(mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

    # just POST permitted
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    permission_classes = [permissions.AllowAny]


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows posts to be viewed or edited.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    # adding owner to post
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

def like(request, post_id):
    add_remove_like(request, post_id)
    return HttpResponseRedirect('http://127.0.0.1:8000/posts/')

def likes_by_date(request, date_interval):
    response =  aggregated_likes_by_date(request, date_interval)
    return response


class LikesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Likes.objects.all()
    serializer_class = LikesSerializer
    permission_classes = [permissions.IsAuthenticated]
