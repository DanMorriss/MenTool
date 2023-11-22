from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Mood


class HomeView(TemplateView):
    template_name = 'tracker/tracker_home.html'


class MoodView(TemplateView):
    template_name = 'tracker/tracker_mood.html'


class StatsView(ListView):
    model = Mood
    template_name = 'tracker/tracker_stats.html'

    def get_queryset(self):
        queryset = Mood.objects.all().order_by('date')
        return queryset


class LandingView(TemplateView):
    template_name = 'tracker/tracker_landing.html'


class AboutUsView(TemplateView):
    template_name = 'tracker/tracker_about_us.html'


class LoginView(TemplateView):
    template_name = 'tracker/tracker_login.html'


class SignUpView(TemplateView):
    template_name = 'tracker/tracker_sign_up.html'
