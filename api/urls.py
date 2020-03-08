from django.urls import path

from api import views

urlpatterns = [
    path('', views.UrlShortenerApiView.as_view(), name='urlshortener_API'),
]
