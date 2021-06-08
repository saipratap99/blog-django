from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,DetailView
from .models import Post
# Create your views here.


# this is function based view
def home(request):
  context = {"posts": Post.objects.all()}
  return render(request,'blog_app/home.html',context)


# creating a class based view for post
# <app_name>/<model>_<listtype>.html
class PostListView(ListView):
  model = Post
  template_name = 'blog_app/home.html'
  # by default it passes context = {'list': Post.objects.all()}
  context_object_name = 'posts'
  ordering = ['-date_posted']

class PostDetailView(DetailView):
  # looks for # <app_name>/<model>_<detail>.html
  # context key name is object
  model = Post


def about(request):
  return render(request,'blog_app/about.html')
