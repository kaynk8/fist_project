from django.urls import path
from sympy import vectorize
from . import views

urlpatterns = [
    path('', views.tutorials, name='tutorial')
]
