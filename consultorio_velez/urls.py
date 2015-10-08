# -*- coding: utf-8 -*-
"""consultorio_velez URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import *
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Administración Dr. Velez Ponce"
admin.site.site_title = "Administración Dr. Velez Ponce"

urlpatterns = [
	url(r'^$', 'especialidades.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^detalle/(?P<slug>[\w-]+)/$', 'especialidades.views.detalle', name='detail-case'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
