# -*- coding: utf-8 -*-

from django import forms


class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file'
    )


class AuthenticationForm(forms.Form):
    userid = forms.CharField(max_length=5, label='User Id: ')
    token = forms.CharField(max_length=80, label='Token: ')

class UploadForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file'
    )

    userid = forms.CharField(max_length=5, label='User Id: ')
    token = forms.CharField(max_length=80, label='Token: ')
