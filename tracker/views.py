from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, FormView
from .forms import MoodForm
from django.utils import timezone

from .forms import UserRegistrationForm, UserLoginForm

from .models import Mood


class HomeView(LoginRequiredMixin, ListView):
    model = Mood
    template_name = 'tracker/tracker_home.html'
    login_url = '/login/'

    def get_queryset(self):
        queryset = Mood.objects.all().order_by('date').filter(
            user=self.request.user)
        return queryset


class MoodView(LoginRequiredMixin, CreateView):
    template_name = 'tracker/tracker_mood.html'
    model = Mood
    success_url = reverse_lazy('stats')
    form_class = MoodForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.date = timezone.now()
        return super().form_valid(form)


class StatsView(ListView):
    model = Mood
    template_name = 'tracker/tracker_stats.html'

    def get_queryset(self):
        queryset = Mood.objects.all().order_by('date').filter(
            user=self.request.user)
        return queryset


class LandingView(TemplateView):
    template_name = 'tracker/tracker_landing.html'


class AboutUsView(TemplateView):
    template_name = 'tracker/tracker_about_us.html'


class SignUpView(CreateView):
    template_name = 'tracker/tracker_sign_up.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


class LoginView(FormView):
    template_name = 'tracker/tracker_login.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)
