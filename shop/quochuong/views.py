from tkinter.messagebox import RETRY
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'pages/home.html')
