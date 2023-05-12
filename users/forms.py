from django import forms
from users.models import CustomUser

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'email',
        ]

class CustomChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = '__all__'

