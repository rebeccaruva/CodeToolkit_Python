from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post # this is hoe we get all attributed from post

# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = 'bloglist.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blogdetail.html'
