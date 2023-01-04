from django import forms
from django.forms import ClearableFileInput
from .models import Trailer, TrailerFiles

class TrailerForm(forms.ModelForm):
    class Meta:
        model = Trailer
        exclude = ['date_created','date_edited','created_by','updated_by']
        # widgets = {
        #     'physical_damage_expiration_date': forms.DateInput(attrs={'type': 'date'}),
        #     'non_trucking_expiration_date': forms.DateInput(attrs={'type': 'date'}),
        #     'cargo_expiration_date': forms.DateInput(attrs={'type': 'date'}),
        #     'registration_start_date': forms.DateInput(attrs={'type': 'date'}),
        #     'registration_expiration_date': forms.DateInput(attrs={'type': 'date'}),
        #     'inspection_expiration_date': forms.DateInput(attrs={'type': 'date'}),
        #     'year_date': forms.DateInput(attrs={'type': 'date'}),
        # }
    def __init__(self, *args, **kwargs):
        super(TrailerForm, self).__init__(*args, **kwargs)
        # self.fields['truck_plate_exp'].required = False
        # self.fields['truck_inspection_exp'].required = False
        self.fields['unit_number'].label = "Unit #"
        self.fields['vin_number'].label = "Vin #"
        self.fields['plate_number'].label = "Plate #"
        self.fields['gps_serial_number'].label = "GPS Serial #"
        self.fields['gps'].label = "GPS"

class TrailerFormUpload(forms.ModelForm):
    class Meta:
        model = TrailerFiles
        fields = [
            'files',
        ]
        widgets = {
            'files': ClearableFileInput(attrs={'multiple': True,"class": "form-control",}),
        }
    def __init__(self, *args, **kwargs):
        super(TrailerFormUpload, self).__init__(*args, **kwargs)
        self.fields['files'].required = False
