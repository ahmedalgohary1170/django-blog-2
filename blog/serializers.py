from rest_framework import serializers

from .models import Post , Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['post', 'author','text','created_at']




class PostSerializer(serializers.ModelSerializer):
    comments= CommentSerializer(many = True, read_only=True)
    class Meta:
        model = Post
        fields = ['id','title', 'description','image', 'created_at','comments']

