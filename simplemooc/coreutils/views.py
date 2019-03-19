from django.shortcuts import render
from django.http import HttpResponse
import getpass


# Create your views here.
def home(request):
    return render(request, 'home.html', {'usuario': getpass.getuser()})

