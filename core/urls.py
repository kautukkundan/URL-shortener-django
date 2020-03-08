from django.urls import path

import core.views as views

urlpatterns = [
    path('', views.UrlShortenerMainView.as_view(), name='all_urls'),
    path('<str:target>/', views.UrlRedirectView.as_view(), name='redirect_urls'),
    path('delete/<int:urlid>/', views.UrlDeleteView.as_view(), name='delete_urls'),
]