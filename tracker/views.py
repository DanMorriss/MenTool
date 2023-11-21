from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'tracker/tracker_home.html'


class MoodView(TemplateView):
    template_name = 'tracker/tracker_mood.html'
