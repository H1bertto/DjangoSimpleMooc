from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views
# from . import views

urlpatterns = [
    path('entrar/', views.auth_login, name='login'),
    # path('entr/', views.contact, name='contact'),
]