from django.contrib.auth.models import User
from users.serializers import UserSerializer, UserCreateSerializer
from rest_framework import permissions, viewsets
from rest_framework import mixins
from rest_framework import generics

# Create your views here.
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