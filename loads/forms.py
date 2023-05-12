from django import forms
from .models import Loads, LoadDelivery, LoadPickup, LoadFiles, LoadDrivers
from django.forms import inlineformset_factory
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Fieldset, Submit
# from crispy_forms.bootstrap import AppendedText, PrependedText, PrependedAppendedText
from django.utils import timezone
class LoadForm(forms.ModelForm):
    class Meta:
        model = Loads
        fields = ['bill_to', 'rate', 'truck', 'trailer', 'po_number', 'load_status', 'starting_address', "notes", "coordinates_starting"]
        widgets = {
            'starting_address': forms.TextInput(attrs={"class": "search-input starting",}),
            'notes': forms.Textarea(attrs={"id": "ckeditor-classic",}),
            'coordinates_starting': forms.HiddenInput
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['rate'].widget.attrs['placeholder'] = '$'
        self.fields['bill_to'].widget.attrs['placeholder'] = 'Bill To'
        
        

# class LoadDeliveryForm(forms.ModelForm):
#     class Meta:
#         model = LoadDelivery
#         fields = ['delivery_location', 'delivery_date_from', 'delivery_date_to']
#         widgets = {
#             'delivery_date_from': forms.DateInput(attrs={'type': 'date'}),
#             'delivery_date_to': forms.DateInput(attrs={'type': 'date'}),
#         }


# class LoadPickupForm(forms.ModelForm):
#     class Meta:
#         model = LoadPickup
#         fields = ['pickup_location', 'pickup_date_from', 'pickup_date_to']
#         widgets = {
#             'pickup_date_from': forms.DateInput(attrs={'type': 'date'}),
#             'pickup_date_to': forms.DateInput(attrs={'type': 'date'}),
#         }
class LoadFilesForm(forms.ModelForm):
    class Meta:
        model = LoadFiles
        fields = ['files']
        widgets = {
            'files': forms.ClearableFileInput(attrs={'multiple': True,"class": "form-control",}),
        }

class LoadDriversForm(forms.ModelForm):
    class Meta:
        model = LoadDrivers
        fields = ['load_driver_user']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['load_user'].widget = forms.CheckboxSelectMultiple()
        self.fields['load_driver_user'].queryset = self.fields['load_driver_user'].queryset.filter(is_driver=True)
        # Exclude drivers who are currently assigned to another load
        # assigned_drivers = Loads.objects.filter(
        #     load_status__in=[Loads.load_status.STATUS_IN_TRANSIT],
        #     load_driver_user__isnull=False,
        #     load_driver_user__is_driver=True,
        #     load_delivery_datetime__gte=timezone.now()
        # ).values_list('load_driver_user__id', flat=True)
        
        # self.fields['load_driver_user'].queryset = self.fields['load_driver_user'].queryset.exclude(id__in=assigned_drivers)


LoadDeliveryFormset = inlineformset_factory(
    Loads,  # parent model
    LoadDelivery,  # child model
    fields=('delivery_location', 'delivery_date_from', 'delivery_date_to', 'coordinates_delivery'),  # fields to include in the formset
    extra=1,  # number of extra forms to display
    can_delete=True,  # enable deleting forms
    widgets={
        'delivery_location': forms.TextInput(attrs={"class": "search-input delivery"}),
        'coordinates_delivery': forms.HiddenInput,
    }
)

LoadPickupFormset = inlineformset_factory(
    Loads,  # parent model
    LoadPickup,  # child model
    fields=('pickup_location', 'pickup_date_from', 'pickup_date_to', 'coordinates_pickup'),  # fields to include in the formset
    extra=1,  # number of extra forms to display
    can_delete=True,  # enable deleting forms
    widgets={
        'pickup_location': forms.TextInput(attrs={"class": "search-input pickup"}),
        'coordinates_pickup': forms.HiddenInput,
        # 'coordinates_pickup': forms.TextInput(attrs={'type': 'hidden'}),
    }
)