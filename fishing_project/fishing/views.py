from django.shortcuts import render
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'fishing/home.html', context)


def about(request):
    return render(request, 'fishing/about.html')
# Create your views here.
