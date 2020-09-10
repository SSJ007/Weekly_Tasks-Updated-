from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.HyperLinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('title','text','created_date', 'salary')
