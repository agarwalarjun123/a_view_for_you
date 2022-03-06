from django import forms
from django.core.exceptions import ValidationError

from .models import User
def password_validator(self,value):
    return False if self.password != value else True


class UserForm(forms.ModelForm):
    password = forms.CharField(required=True,widget=forms.PasswordInput(), label='password')
    confirmPassword = forms.CharField(required=True,widget=forms.PasswordInput(), label='confirm your password')

    def clean_confirmPassword(self):
        if self.cleaned_data['password'] != self.cleaned_data['confirmPassword']:
            raise ValidationError('passwords did not Match.')

    class Meta:
        model = User
        fields = ('profile_image','username','email','password')
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
