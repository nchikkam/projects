# -*- coding: utf-8 -*-
from django.conf.urls import url
from myproject.storage.views import list, auth, upload

urlpatterns = [
    url(r'^list/$', list, name='list'),
    url(r'^auth/$', auth, name='auth'),
    url(r'^upload/$', upload, name='upload')
]