# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage

import os


def content_file_name(instance, filename):
    name, ext = filename.split('.')
    file_path = 'documents/{userid}/{token}/{directory}/{name}.{ext}'.format(
        userid=instance.userid, token=instance.token, name=name, ext=ext, directory="user_directory")
    return file_path

class OverwriteStorage(FileSystemStorage):

    def __init__(self):
        super(OverwriteStorage, self).__init__()

    def get_available_name(self, name):
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name

class Document(models.Model):

    #docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    docfile = models.FileField(upload_to=content_file_name, storage=OverwriteStorage(), max_length=None)

    userid = models.CharField(max_length=8)
    token = models.CharField(max_length=80)
