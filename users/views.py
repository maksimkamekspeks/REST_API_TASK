from django.contrib.auth.models import User
from users.serializers import UserSerializer, UserCreateSerializer
from rest_framework.decorators import action
from django.utils import timezone
from rest_framework.response import Response
from rest_framework import permissions, viewsets, generics, status, mixins
from api.models import Likes

# Create your views here.
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=True)
    def user_activity(self, request, pk=None):
        user = self.get_object()
        user_last_login = user.last_login
        response = user_last_login.strftime('%y-%m-%d %a %H:%M:%S')
        return Response(response)


class UserCreateViewSet(mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

    # just POST permitted
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    permission_classes = [permissions.AllowAny]