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
from especialidades.views import *


admin.site.site_header = "Administración Dr. Velez Ponce"
admin.site.site_title = "Administración Dr. Velez Ponce"

urlpatterns = [
	url(r'^$', IndexView.as_view(), name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^caso/(?P<slug>[\w-]+)/$', CasoDetail.as_view(), name='detail-case'),
    url(r'^lista-casos/$', ListCasosView.as_view(), name='lista_casos'),
    url(r'^contacto/$', contacto, name='contacto'),
    url(r'^expedientes/$', ListExpedientesView.as_view(), name='expedientes'),
    url(r'^expediente/(?P<slug>[\w-]+)/$', detail_expediente, name='detail-exp'),
    url(r'^resumenes-clinicos/$', ListResumenesView.as_view(), name='resumenes-clinicos'),
    url(r'^resumenes-clinicos/(?P<slug>[\w-]+)/$', detail_resumen, name='resumen-clinico-detail'),
    url(r'^resumen-clinico-pdf/(?P<id>[0-9]+)/$', resumen_pdf, name='pdf_resumen'),
    url(r'^tratamiento-pdf/(?P<id>[0-9]+)/$', tratamiento_pdf, name='pdf_tratamiento'),
    #filtros
    url(r'^casos-ortopedia/$', ListOrtopediaView.as_view(), name='ortopedia'),
    url(r'^casos-trauma/$', ListTraumaView.as_view(), name='trauma'),
    url(r'^casos-artroscopia/$', ListArtroscopiaView.as_view(), name='artroscopia'),
    url(r'^casos-cirugia-biologica/$', ListCirugia_BiologicaView.as_view(), name='cirugia_biologica'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
