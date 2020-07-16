from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import JsonResponse
from .models import Post
from . import secrets
from users import models
import requests


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'fishing/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'fishing/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):

    model = Post
    fields = ['title', 'location', 'fish', 'size', 'lure']
    
    def form_valid(self, form):
        
        url = 'https://maps.googleapis.com/maps/api/geocode/json'
        response = requests.get(url, params={
            'address': form.instance.location,
            'key': secrets.google_api_key
        })
        data = response.json()
       
        location = data['results'][0]['geometry']['location']
        form.instance.latitude = location['lat']
        form.instance.longitude = location['lng']
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'location', 'fish', 'size', 'lure']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'fishing/about.html')
# Create your views here.
def supply(request):
    return render(request, 'fishing/supply.html')

def spot(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
        'google_api_key': secrets.google_api_key
    }
    return render(request, 'fishing/spot.html', context)


def locations(request):
    locations = []
    for post in Post.objects.all():
        location = {
            'label': post.location,
            'lat': post.latitude,
            'lng': post.longitude,
        }
        
        locations.append(location)
    return JsonResponse({'locations': locations})

def camping(request):
    return render(request, 'fishing/camping.html')

def calendar(request):
    return render(request, 'fishing/calendar.html')
