from django import forms


class ProfileFrom(forms.Form):
    first_name = forms.CharField(max_length=30, Lavel='family name')
    last_name = forms.CharField(max_length=30, Lavel='last name')
    department = forms.CharField(max_length=30, Lavel='department', required=False)
