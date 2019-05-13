# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()


class RegistraForm(forms.ModelForm):

    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmação de Senha', widget=forms.PasswordInput)

    def clean_password(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('As Senhas não estão iguais')

        return password2

    def save(self, commit=True):
        user = super(RegistraForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        # user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['username', 'email']

    # email = forms.EmailField(label='E-mail')
    # def clean_email(self):
    #     email = self.cleaned_data['email']
    #     if User.objects.filter(email=email).exists():
    #         raise forms.ValidationError('Já existe usuário cadastrado com este E-Mail')
    #     return email


class EditAccountForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'name']
