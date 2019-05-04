from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import authenticate, login
from .forms import RegistraForm


def register(request):
    template_name = 'accounts/register.html'
    if request.method == 'POST':
        form = RegistraForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(
                username=user.username,
                password=form.cleaned_data['password1']
            )
            login(request, user)
            return redirect('coreutils:home')

    else:
        form = RegistraForm()
    context = {
        'form': form,
    }
    return render(request, template_name, context)


def dashboard(request):
    template_name = 'accounts/dashboard.html'
    return render(request, template_name)
