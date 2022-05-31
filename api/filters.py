import django_filters
from django.db import models as django_models
from django_filters import rest_framework as filters
from api.models import Likes

class LikesFilter(filters.FilterSet):
    class Meta:
        model = Likes
        fields = {
            'created': ('lte', 'gte')
        }

    filter_overrides = {
        django_models.DateTimeField: {
            'filter_class': django_filters.IsoDateTimeFilter
        },
    }
