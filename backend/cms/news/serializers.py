from rest_framework import serializers

from .models import Link, Group
from .models import (
    NewsContent,
    NewsPost,
)


class NewsContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsContent
        fields = [
            "id",
            "content_type",
            "content_text",
            "content_image",
            "content_video",
            "caption",
            "order",
        ]


class NewsPostSerializer(serializers.ModelSerializer):
    contents = NewsContentSerializer(many=True, read_only=True)

    class Meta:
        model = NewsPost
        fields = ["id", "title", "created_at", "updated_at", "contents"]


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ['id', 'title', 'url', 'created_at']


class GroupSerializer(serializers.ModelSerializer):
    links = LinkSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = ['id', 'name', 'created_at', 'links']
