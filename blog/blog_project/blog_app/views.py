from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy

class BlogListView(ListView):
    model=Post
    template_name = 'blog_app/post_list.html'
    context_object_name = "parsed_object_for_list_view"

class BlogDetailView(DetailView):
    model=Post
    template_name='blog_app/post_detail.html'
    context_object_name = 'parsed_object_for_detail_view'

class BlogCreateView(CreateView):
	model=Post
	template_name='blog_app/post_new.html'
	fields='__all__'

class BlogUpdateView(UpdateView):
    model = Post
    fields = ['title','text']
    template_name = "blog_app/post_edit.html"
class BlogDeleteView(DeleteView):
    model = Post
    template_name = "blog_app/post_delete.html"
    success_url = reverse_lazy("post_list")


# Create your views here.

