from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

class Home_page_view(TemplateView):
	template_name='staticpages/index.html'

class About_view(TemplateView):
	template_name='staticpages/about.html'
