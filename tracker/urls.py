from django.urls import path
from tracker import views


urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('mood/', views.MoodView.as_view(), name='mood-form'),
    path('stats/', views.StatsView.as_view(), name='stats'),
    path('', views.LandingView.as_view(), name='landing'),
    path('about-us/', views.AboutUsView.as_view(), name='about-us'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
]
