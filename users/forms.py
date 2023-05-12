from django import forms
from users.models import CustomUser

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'email',
<<<<<<< HEAD
        ]

class CustomChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = '__all__'

=======
        ]
>>>>>>> 588876d0dc8d4fce8bd7cad04e372aa75d08343d
