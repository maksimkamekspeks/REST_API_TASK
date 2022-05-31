from users.models import UsersInformation
from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin

class LastActionMiddleware(MiddlewareMixin):

    def process_request(self, request):
        user_last_action = UsersInformation(user=request.user, last_request=timezone.now())
        user_last_action.save()
