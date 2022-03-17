from django.urls import path
from profile import views

app_name = 'profile'

urlpatterns = [
    path('', views.show_profile, name='profile'),
    path('likes/', views.show_profile_likes, name='profile_likes'),
    path('reviews/', views.show_profile_reviews, name='profile_reviews'),
]
