from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
  {
    'author': 'Sai Pratap',
    'title' : 'First post',
    'content': "Sai pratap's first post",
    'date_posted' : '27th Aug 2021'
  },
  {
    'author': 'Tarun',
    'title' : 'First post',
    'content': "Tarun's first post",
    'date_posted' : '13th Aug 2021'
  }
]

def home(request):
  context = {
    'posts': posts,
    'title' : 'home'
  }
  return render(request,'blog_app/home.html',context)

def about(request):
  return render(request,'blog_app/about.html')
