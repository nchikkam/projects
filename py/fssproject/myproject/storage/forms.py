# -*- coding: utf-8 -*-

from django import forms

class DocumentForm(forms.Form):
    userid = forms.CharField(max_length=5, label='User Id: ')
    token = forms.CharField(max_length=80, label='Token: ')

    docfile = forms.FileField( label='Select a file' )