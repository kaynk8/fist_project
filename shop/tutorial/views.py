from django.shortcuts import render

from django.http import HttpResponse

def tutorials(request):
    return render(request, 'pages/tutorials.html')
