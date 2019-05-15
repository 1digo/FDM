"""FDM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.contrib.staticfiles.views import serve
from django.urls import path, re_path, include
from django.views.generic import RedirectView
from rest_framework.routers import SimpleRouter

from fdm.apps.accounts.api.v1.viewsets import AccountViewSet


api_v1_router = SimpleRouter()
api_v1_router.register('users', AccountViewSet)

api_v1_urlpatterns = [
    path('v1/auth/', include('rest_auth.urls')),
    path('v1/', include((api_v1_router.urls, 'v1'), namespace='v1')),
]



urlpatterns = [
    path('', serve, kwargs={'path': 'frontend/index.html'}),
    re_path('^(?!/?static/)(?!/?media/)(?P<path>.*\..*)$',
            RedirectView.as_view(url='/static/frontend/%(path)s', permanent=False)),
    path('admin/', admin.site.urls),
    path('api/', include((api_v1_urlpatterns, 'api_v1'), namespace='api')),
    path('api-auth/', include('rest_framework.urls')),
]
