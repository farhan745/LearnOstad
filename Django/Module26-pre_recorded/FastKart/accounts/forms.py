from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordResetForm,SetPasswordForm,UserChangeForm

class CustomUserCreationsForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')
        
class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')
        
class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(required=True)
    
class CustomSetPasswordForm(SetPasswordForm):
    class Meta:
        model = CustomUser
        fields = ('new_password1', 'new_password2')
        
class CustomUserChangeForm(UserChangeForm):
    password = None
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name')
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['username'].widget.attrs.update({'class':'form-control'})
            self.fields['email'].widget.attrs.update({'class':'form-control'})
            self.fields['first_name'].widget.attrs.update({'class':'form-control'})
            self.fields['last_name'].widget.attrs.update({'class':'form-control'})