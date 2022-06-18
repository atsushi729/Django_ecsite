from django import forms
from allauth.account.forms import SignupForm


class SignupSellerForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='family_name')
    last_name = forms.CharField(max_length=30, label='last_name')

    def save(self, request):
        user = super(SignupSellerForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user
