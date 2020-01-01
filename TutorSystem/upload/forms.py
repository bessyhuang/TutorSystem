from django import forms
from .models import *

class File_UploadForm(forms.ModelForm):
    class Meta:
        model = File_Upload
        fields = ['title', 'slug', 'body', 'upload_date', 'upload_files']