from api.models import Post, Likes
from rest_framework import serializers

class PostSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source = 'owner.username')
    class Meta:
        model = Post
        fields = ['url', 'id', 'owner', 'title', 'created', 'info', 'liked_by']
        ordering = ['created']

    def create(self, validated_data):
        owner = self.context['request'].user
        post = Post.objects.create(owner=owner, **validated_data)
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return post


class LikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = ['post', 'user', 'created']
        ordering = ['created']
