from django.urls import path
from sympy import vectorize
from . import views

urlpatterns = [
    path('', views.contact, name='contact')

]
