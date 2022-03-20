from django import forms
from authentication.models import User

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('profile_image','introduction')
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'