from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from api import views

urlpatterns = [
    path('', views.UrlShortenerApiView.as_view(), name='urlshortener_API'),
    path('auth/', obtain_auth_token, name='rest-api-auth')
]
