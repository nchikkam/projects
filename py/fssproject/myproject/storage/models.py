# -*- coding: utf-8 -*-
from django.db import models


def content_file_name(instance, filename):
    name, ext = filename.split('.')
    file_path = 'documents/{userid}/{token}/{directory}/{name}.{ext}'.format(
        userid=instance.userid, token=instance.token, name=name, ext=ext)
    return file_path

class Document(models.Model):

    #docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    docfile = models.FileField(upload_to=content_file_name)
    userid = models.CharField(max_length=8, default='1')
    token = models.CharField(max_length=80, default='00000000')


class User(models.Model):
    #id = models.IntegerField(primary_key=True)
    userid = models.CharField(max_length=8)
    token = models.CharField(max_length=80)
