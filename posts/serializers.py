from rest_framework import serializers
from posts.models import Post
from posts.models import Comment

from django.contrib.auth.models import User

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment

class PostSerializer(serializers.ModelSerializer):
    user = serializers.Field(source = "user.username")

    # comments = serializers.RelatedField(many = True)
    # comments = CommentSerializer(many = True)
    class Meta:
        model = Post
        fields = ('user', 'id', 'title', 'content',)

class UserSerializer(serializers.ModelSerializer):
    # posts = serializers.PrimaryKeyRelatedField(many = True)
    # posts = PostSerializer(many = True)

    class Meta:
        model = User
        fields = ('id', 'username',)
