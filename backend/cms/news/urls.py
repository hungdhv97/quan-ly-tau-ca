from django.urls import (
    include,
    path,
)
from rest_framework.routers import DefaultRouter

from .views import (
    NewsContentViewSet,
    NewsPostViewSet, LinkViewSet, GroupViewSet,
)

router = DefaultRouter()
router.register(r"news-posts", NewsPostViewSet, basename="news-post")
router.register(r"news-contents", NewsContentViewSet, basename="news-content")
router.register(r"links", LinkViewSet, basename="links")
router.register(r'groups', GroupViewSet, basename='groups')

urlpatterns = [
    path("", include(router.urls)),
]
