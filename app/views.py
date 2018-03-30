from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from .models import Blog

class HomeView(TemplateView):
    template_name = "home.html"


class BlogView(ListView):
    model = Blog
    paginate_by = 4
    template_name = "blog.html"


class ContactView(TemplateView):
    template_name="contact.html"