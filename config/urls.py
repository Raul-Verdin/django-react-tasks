"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
# config/urls.py
from django.contrib import admin
from django.views.generic import TemplateView

from django.urls import path, include, re_path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from apps.tasks.views import csrf

urlpatterns = [
    path("admin/", admin.site.urls),

    # Exponiendo rutas desde apps.tasks:
    path("api/v1/", include("apps.tasks.urls")),

    # Endpoint para obtener cookie CSRF:
    path("api/csrf/", csrf, name="csrf"),

    # Documentación:
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),

    # Rutas para React SPA
    path("", TemplateView.as_view(template_name="index.html"), name="index"),
    re_path(r"^.*$", TemplateView.as_view(template_name="index.html")),
]
