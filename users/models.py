from django.db import models

class UsersInformation(models.Model):
    user = models.CharField(max_length=100, blank=True, default='')
    last_request = models.DateTimeField(auto_now_add=True)
