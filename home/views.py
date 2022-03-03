from django.shortcuts import render

# Create your views here.

def homepage(request):
    if request.method == 'GET':
        return render(request, 'home/homepage.html')