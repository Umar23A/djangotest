from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "index.html"

class AboutView(TemplateView):
    template_name = "about.html"
