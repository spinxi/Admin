from django import forms
from django.forms import ClearableFileInput
from users.models import CustomUser
from .models import Trucks, TruckFiles

class TrucksForm(forms.ModelForm):
    who_is_driver = forms.ModelChoiceField(queryset=CustomUser.objects.filter(is_driver=True), empty_label=None)
    who_is_driver_ezpass = forms.ModelChoiceField(queryset=CustomUser.objects.filter(is_driver=True), empty_label=None)
    class Meta:
        model = Trucks
        exclude = ['date_created','date_edited','created_by','updated_by']
    def __init__(self, *args, **kwargs):
        super(TrucksForm, self).__init__(*args, **kwargs)
        self.fields['status'].required = False
        # self.fields['truck_inspection_exp'].required = False

class TruckFormUpload(forms.ModelForm):
    class Meta:
        model = TruckFiles
        fields = [
            'files',
        ]
        widgets = {
            'files': ClearableFileInput(attrs={'multiple': True,"class": "form-control",}),
        }
