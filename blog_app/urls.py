from django.urls import path
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post-details'),
    path('post/new/',PostCreateView.as_view(),name='post-create'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),
    path('about/', views.about, name='blog-about'),
]

# all routes must end with trailing forward slash
# PostListView.as_view() looks for <app_name>/<model>_<listtype>.html
