from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions, viewsets, generics, status, mixins
from users.serializers import UserSerializer, UserCreateSerializer
from users.models import UsersInformation

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=True)
    def user_activity(self, request, pk=None):
        user = self.get_object()
        user_last_login = user.last_login
        last_login_time = user_last_login.strftime('%y-%m-%d %a %H:%M:%S')
        user_info = UsersInformation.objects.filter(user=user).last()
        last_user_action = user_info.last_request.strftime('%y-%m-%d %a %H:%M:%S')
        return Response({'last-login': last_login_time, 'last_action': last_user_action})

class UserCreateViewSet(mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

    # just POST permitted
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    permission_classes = [permissions.AllowAny]