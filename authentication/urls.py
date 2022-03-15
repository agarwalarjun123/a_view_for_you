from .views import login, register, logout
from django.urls import path

app_name = 'auth'
urlpatterns = [
    path('register/',register, name = 'register'),
    path('login/',login, name = 'login'),
    path('logout/', logout, name = 'logout')
]