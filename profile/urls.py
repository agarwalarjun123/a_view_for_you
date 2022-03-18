from django.urls import path
from profile import views

app_name = 'profile'

urlpatterns = [
    path('', views.show_profile, name='profile'),
]
