from django import forms
from . import models


class image_upload(forms.ModelForm):
    class Meta:
        model=models.Upload
        fields=["image","img_name"]
