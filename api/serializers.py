from django.contrib.auth.models import User
from api.models import Post, Likes
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(many=True, view_name='post-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'posts']

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    # adding new user to database
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )
        return user

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'password']


class PostSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Post
        fields = ['url', 'id', 'owner', 'title', 'created', 'info', 'liked_by']
        ordering = ['created']


class LikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = ['post', 'user', 'created']
        ordering = ['created']
