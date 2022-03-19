from django.urls import path
from landscape import views

app_name = 'landscape'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name = 'search'),
    path('<slug:landscape_name_slug>/', views.show_landscape, name='show_landscape'),
    path('<slug:landscape_name_slug>/add_review/', views.add_review, name='add_review'),
    path('<slug:landscape_name_slug>/like', views.add_like, name='add_like'),
]