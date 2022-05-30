from api.models import Post, Likes
from django.shortcuts import get_object_or_404
from django.utils import timezone


# def add_remove_like(request, post_id):
#     post = get_object_or_404(Post, id=post_id)
#     user = request.user
#     users_like = Likes.objects.filter(post=post, user=user)
#     if users_like:
#         Likes.objects.filter(post=post, user=user).delete()
#         post.liked_by.remove(user)
#     else:
#         like = Likes(post=post, user=user, created=timezone.now())
#         like.save()
#         post.liked_by.add(user)
#     post.save()


# ?date_from=2020-02-02&date_to=2020-02-15
# ?created_gte=2020-02-02&created_lte=2020-02-15
