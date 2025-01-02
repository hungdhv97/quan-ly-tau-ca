from rest_framework import viewsets

from .models import Group, Link
from .models import (
    NewsContent,
    NewsPost, )
from .serializers import GroupSerializer, LinkSerializer
from .serializers import (
    NewsContentSerializer,
    NewsPostSerializer, )


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.prefetch_related('links').all()
    serializer_class = GroupSerializer


class NewsPostViewSet(viewsets.ModelViewSet):
    queryset = NewsPost.objects.all()
    serializer_class = NewsPostSerializer


class NewsContentViewSet(viewsets.ModelViewSet):
    queryset = NewsContent.objects.all()
    serializer_class = NewsContentSerializer


class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
