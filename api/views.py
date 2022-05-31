from api.models import Post, Likes
from api.serializers import PostSerializer, LikesSerializer
from api.permissions import IsOwnerOrReadOnly
from rest_framework import permissions, viewsets, generics, status
from rest_framework.decorators import action
from django.utils import timezone
from rest_framework.response import Response
from api.filters import LikesFilter

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    @action(detail=True)
    def add_like(self, request, pk=None):
        post = self.get_object()
        user = request.user
        users_like = Likes.objects.filter(post=post, user=user)
        if not users_like:
            like = Likes(post=post, user=user, created=timezone.now())
            like.save()
            post.liked_by.add(user)
            post.save()
            return Response({'status': 'post has liked'})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True)
    def remove_like(self, request, pk=None):
        post = self.get_object()
        user = request.user
        users_like = Likes.objects.filter(post=post, user=user)
        if users_like:
            Likes.objects.filter(post=post, user=user).delete()
            post.liked_by.remove(user)
            post.save()
            return Response({'status': 'post has disliked'})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class LikesList(generics.ListAPIView):
    queryset = Likes.objects.all()
    serializer_class = LikesSerializer
    filter_class = LikesFilter
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = Likes.objects.all()
        queryset = queryset.filter(user=user)
        return queryset
        # queryset = Likes.objects.all()
        # date_from = self.request.query_params.get('date_from', None)
        # date_to = self.request.query_params.get('date_to', None)
        # if (date_from is not None) and (date_to is not None):
        #     queryset = queryset.filter(created__gte=date_from).filter(created__lte=date_to)
        # return queryset



