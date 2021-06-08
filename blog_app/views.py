from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import (
          ListView,
          DetailView,
          CreateView,
          UpdateView,
          DeleteView)
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
  # looks for # <app_name>/<model>_detail.html
  # context key name is object
  model = Post

class PostCreateView(LoginRequiredMixin,CreateView):
  # looks for # <app_name>/<model>_form.html
  # context key name is object
  model = Post
  fields = ['title','content']

  def form_valid(self,form):
    form.instance.auth = self.request.user
    return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
  # uses same post_form.html
  # looks for # <app_name>/<model>_form.html
  # context key name is object
  model = Post
  fields = ['content']

  def form_valid(self,form):
    form.instance.auth = self.request.user
    return super().form_valid(form)

  # in order to update the post only by the author
  def test_func(self):
    post = self.get_object()  # current post
    if self.request.user == post.auth:
      return True
    else:
      return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
  # post_confirm_delete.html
  model = Post
  success_url = '/'

  # in order to delete the post only by the author
  def test_func(self):
    post = self.get_object()  # current post
    if self.request.user == post.auth:
      return True
    else:
      return False



def about(request):
  return render(request,'blog_app/about.html')
