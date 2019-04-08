from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('<int:pk>/', views.details, name='details'),
    # path('<string:slug>/', views.details, name='details'),
    # re_path('^(?P<pk>\d+)/$', views.details, name='details'),
    re_path('^(?P<slug>[\w_-]+)/$', views.details, name='details'),
    # path('contato/', views.courses, name='index'),
]
