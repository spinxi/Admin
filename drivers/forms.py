from django import forms
from django.forms import ClearableFileInput
from drivers.models import Driver, DriversFiles

class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        exclude = [
            'full_name',
        ]
        
class DriverFormUpload(forms.ModelForm):
    class Meta:
        model = DriversFiles
        fields = [
            'file',
        ]
        widgets = {
            'file': ClearableFileInput(attrs={'multiple': True,"class": "form-control",}),
        }