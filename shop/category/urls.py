from urllib.parse import urlparse
from django.urls import path
from sympy import vectorize
from . import views

urlpatterns = [
    path('', views.category, name='category')
]
