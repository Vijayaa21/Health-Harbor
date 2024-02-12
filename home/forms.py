from django import forms
from .models import medicalRecord


class ImageUploadForm(forms.Form):
    image = forms.ImageField(label='Upload Image')

class medicalRecordForm(forms.ModelForm):
    class Meta:
        model = medicalRecord
        fields = ['image']