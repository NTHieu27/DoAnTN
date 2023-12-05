from django import forms
from .models import User


class ProfileEditForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    date_of_birth = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    bio = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    website = forms.URLField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    location = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))


    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'date_of_birth', 'phone_number', 'bio', 'website', 'location',
                  'image']
        exclude = ['date_modified']

    def __init__(self, *args, **kwargs):
        super(ProfileEditForm, self).__init__(*args, **kwargs)
