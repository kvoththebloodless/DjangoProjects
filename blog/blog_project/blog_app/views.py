from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView

class BlogListView(ListView):
    model=Post
    template_name = 'blog_app/post_list.html'
    context_object_name = "parsed_object_for_list_view"

class BlogDetailView(DetailView):
    model=Post
    template_name='blog_app/post_detail.html'
    context_object_name = 'parsed_object_for_detail_view'

# Create your views here.

