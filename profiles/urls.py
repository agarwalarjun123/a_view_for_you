from django.urls import path
from . import views

app_name = 'profile'

urlpatterns = [
    path('', views.show_profile, name='profile'),
    path('edit/', views.edit_profile, name='edit'),
]
