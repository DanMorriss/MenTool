from django.urls import path
from tracker import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
]
