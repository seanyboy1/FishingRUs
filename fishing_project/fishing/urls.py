from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views


urlpatterns = [
    path('', PostListView.as_view(), name='fishing-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='fishing-about'),
    path('supply/', views.supply, name='fishing-supply'),
    path('spot/', views.spot, name='fishing-spot'),
    path('camping/', views.camping, name='fishing-camping'),
    path('calendar/', views.calendar, name='fishing-calendar'),
]