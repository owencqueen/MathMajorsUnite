from django import forms
from .models import Images

class ImagesForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ('title', 'img_zip')