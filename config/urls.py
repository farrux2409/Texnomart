"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf.urls.static import static

import app
import accounts
from config import settings
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from django.contrib import admin
from django.urls import path, include

if settings.DEBUG:
    import debug_toolbar
urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('texnomart-uz/', include('app.urls')),
                  path('api-auth/', include('rest_framework.urls')),
                  path('accounts/', include('accounts.urls')),
                  path('api-token-auth/', views.obtain_auth_token),
                  path('__debug__/', include(debug_toolbar.urls)),


              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.conf import settings
from debug_toolbar.toolbar import debug_toolbar_urls
