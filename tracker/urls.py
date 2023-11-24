from django.urls import path
from tracker import views


urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('mood/', views.MoodView.as_view(), name='mood-form'),
    path('stats/', views.StatsView.as_view(), name='stats'),
    path('', views.LandingView.as_view(), name='landing'),
    path('about-us/', views.AboutUsView.as_view(), name='about-us'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('mood/<int:pk>/', views.MoodDetailView.as_view(), name='mood-detail'),
    path('mood/<int:pk>/update/', views.UpdateMoodView.as_view(), name='update-mood'),
    path('mood/<int:pk>/delete/', views.DeleteMoodView.as_view(), name='delete-mood'),
    path('account/delete/', views.DeleteAccontView.as_view(), name='delete-account'),
]
