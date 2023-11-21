from django.urls import path
from tracker import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('mood/', views.MoodView.as_view(), name='mood-form')
]
