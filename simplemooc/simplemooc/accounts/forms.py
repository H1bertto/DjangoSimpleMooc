from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistraForm(UserCreationForm):

    email = forms.EmailField(label='E-mail')

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Já existe usuário cadastrado com este E-Mail')
        return email

    def save(self, commit=True):
        user = super(RegistraForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
