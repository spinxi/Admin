from django import forms
from django.forms import ModelForm, ClearableFileInput
from loads.models import Loads, LoadFiles, LoadDrivers
from django.forms import inlineformset_factory
# from crispy_forms.helper import FormHelper
# from crispy_forms.bootstrap import PrependedText
# from crispy_forms.layout import Layout
from users.models import CustomUser
class LoadForm(ModelForm):
    class Meta:
        model = Loads
        exclude = ["created_by", "updated_by"]
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.layout = Layout(
    #         PrependedText('rate', '$', placeholder="Enter Email Address"),
    #     )

class LoadFormUpload(forms.ModelForm):
    class Meta:
        model = LoadFiles
        fields = [
            'files',
        ]
        widgets = {
            'files': ClearableFileInput(attrs={'multiple': True,"class": "form-control",}),
        }

class LoadDriversForm(forms.ModelForm):
    load_drivers = forms.ModelChoiceField(queryset=CustomUser.objects.filter(is_driver=True))
    class Meta:
        model = LoadDrivers
        fields = [
            "load_drivers","load_driver_type",
        ]

BookFormSet = inlineformset_factory(
    model = LoadDrivers,
    parent_model = Loads,
    # form = LoadDriversForm,
    fields = [
        "load_drivers","load_driver_type",
    ],
    min_num=1,  # minimum number of forms that must be filled in
    extra=1,  # number of empty forms to display
    can_delete=False  # show a checkbox in each form to delete the row
)