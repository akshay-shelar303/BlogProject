from rest_framework import serializers

from .models import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"

    def create(self, validated_data):
        return Blog.objects.create(**validated_data)
