from .views import login, register
from django.urls import path

app_name = 'auth'
urlpatterns = [
    path('register/',register, name = 'register'),
    path('login/',login, name = 'login')
]