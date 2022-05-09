from django import forms


class ProfileForm(forms.Form):
    first_name = forms.CharField(max_length=30, label='family_name')
    last_name = forms.CharField(max_length=30, label='last_name')
    department = forms.CharField(max_length=30, label='department', required=False)
