from api.views import UrlShortenerApiViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register('urls', UrlShortenerApiViewSet, basename='UrlAPI')