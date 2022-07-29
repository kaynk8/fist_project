from django.shortcuts import render
from django.http import HttpResponse



def category(request):
    return render(request, 'pages/category.html')
