from django import forms
from django.forms import ClearableFileInput
from drivers.models import Driver, DriversFiles

class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        exclude = [
<<<<<<< HEAD
            "driver_user"
=======
            'full_name',
>>>>>>> 588876d0dc8d4fce8bd7cad04e372aa75d08343d
        ]
        
class DriverFormUpload(forms.ModelForm):
    class Meta:
        model = DriversFiles
<<<<<<< HEAD
        exclude = [
            'driver_files',
        ]
        widgets = {
            'ben_file': ClearableFileInput(attrs={'multiple': True,"class": "form-control",}),
            'application_file': ClearableFileInput(attrs={'multiple': True,"class": "form-control",}),
            'bank_file': ClearableFileInput(attrs={'multiple': True,"class": "form-control",}),
            'w9_file': ClearableFileInput(attrs={'multiple': True,"class": "form-control",}),
            'pev_file': ClearableFileInput(attrs={'multiple': True,"class": "form-control",}),
            'contract_file': ClearableFileInput(attrs={'multiple': True,"class": "form-control",}),
            'mvr_file': ClearableFileInput(attrs={'multiple': True,"class": "form-control",}),
            'medical_file': ClearableFileInput(attrs={'multiple': True,"class": "form-control",}),
            'occ_file': ClearableFileInput(attrs={'multiple': True,"class": "form-control",}),
            'license_file': ClearableFileInput(attrs={'multiple': True,"class": "form-control",}),
            'drug_test_file': ClearableFileInput(attrs={'multiple': True,"class": "form-control",}),
=======
        fields = [
            'file',
        ]
        widgets = {
            'file': ClearableFileInput(attrs={'multiple': True,"class": "form-control",}),
>>>>>>> 588876d0dc8d4fce8bd7cad04e372aa75d08343d
        }