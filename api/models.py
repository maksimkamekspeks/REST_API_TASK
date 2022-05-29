from django.db import models


# Create your models here.
class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    info = models.TextField()
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE, default='admin')
    liked_by = models.ManyToManyField('auth.User', through='Likes', through_fields=('post', 'user'),)

    class Meta:
        ordering = ['created']

class Likes(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
