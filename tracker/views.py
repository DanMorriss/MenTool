from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'tracker/tracker_home.html'


class MoodView(TemplateView):
    template_name = 'tracker/tracker_mood.html'


class StatsView(TemplateView):
    template_name = 'tracker/tracker_stats.html'


class LandingView(TemplateView):
    template_name = 'tracker/tracker_landing.html'


class AboutUsView(TemplateView):
    template_name = 'tracker/tracker_about_us.html'


class LoginView(TemplateView):
    template_name = 'tracker/tracker_login.html'


class SignUpView(TemplateView):
    template_name = 'tracker/tracker_sign_up.html'
