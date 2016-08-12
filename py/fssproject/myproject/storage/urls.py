# -*- coding: utf-8 -*-
from django.conf.urls import url
from myproject.storage.views import service

urlpatterns = [
    url(r'^service/$', service, name='service'),
]