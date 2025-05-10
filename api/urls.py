"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import (
    CreateShortUrlView, 
    RetreiveShortUrlView, 
    UpdateShortUrlView, 
    DeleteShortUrlView, 
    ShortUrlRedirectView,
    GetshortUrlStatisticsView
    )

urlpatterns = [
    path('create/', CreateShortUrlView.as_view(), name='create_short_url'),
    path('retreive/<str:shortcode>', RetreiveShortUrlView.as_view(), name='retreive_short_url'),
    path('update/<str:shortcode>', UpdateShortUrlView.as_view(), name='update_short_url'),
    path('delete/<str:shortcode>', DeleteShortUrlView.as_view(), name='delete_short_url'),
    path('<str:shortcode>', ShortUrlRedirectView.as_view(), name='short-url-redirect'),
    path('<str:shortcode>/status', GetshortUrlStatisticsView.as_view(), name='short-url-status'),
]
