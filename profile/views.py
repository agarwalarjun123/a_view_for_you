from django.shortcuts import render

def profile(request):
    if request.method == 'GET':
        return render(request, 'profile/profile.html')
