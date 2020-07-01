from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='fishing-home'),
    path('about/', views.about, name='fishing-about'),
]