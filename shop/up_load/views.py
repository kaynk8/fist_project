from django.shortcuts import render

from up_load.models import Post

def list(request):
    data = {'Post': Post.objects.all().order_by('-date')}
    return render(request, 'pages/up_load.html', data)
    