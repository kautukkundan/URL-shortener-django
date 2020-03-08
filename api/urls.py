from django.urls import path

from api import views

urlpatterns = [
  path('', views.UrlShortenerApiView, name='urlshortener_API'),
]
