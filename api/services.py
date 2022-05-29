from datetime import datetime

from api.models import Post, Likes
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.http import JsonResponse


def add_remove_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user
    users_like = Likes.objects.filter(post=post, user=user)
    if users_like:
        Likes.objects.filter(post=post, user=user).delete()
        post.liked_by.remove(user)
    else:
        like = Likes(post=post, user=user, created=timezone.now())
        like.save()
        post.liked_by.add(user)
    post.save()

def aggregated_likes_by_date(request, date_interval):
    # user = request.user
    # lower = ""
    # likes = Likes.objects.filter(created__gt=datetime.date(year_low, month_low, day_low)).filter(created__lt=datetime.date(year_top, month_top, day_top))
    # amount = 0
    # for _ in likes:
    #     amount += 1
    # info = {'amount_of_likes': amount}
    # return JsonResponse(info)
    return JsonResponse({'foo': date_interval})

# ?date_from =2020-02-02&date_to=2020-02-15
