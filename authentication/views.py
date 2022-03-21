from django.shortcuts import redirect, render
from .forms import UserForm
from django.contrib.auth import authenticate, login as login_session, logout as logout_session
from django.contrib.auth.decorators import login_required
from django.apps import apps as django_apps


def register(request):
    userForm = {}
    if request.method == 'GET':
        userForm = UserForm()
    if request.method == 'POST':
        userForm = UserForm(request.POST)
        if userForm.is_valid():
            user = userForm.save(commit=False)
            if 'profile_image' in request.FILES:
                user.profile_image = request.FILES['profile_image']
            user.set_password(user.password)
            user.save()
            return redirect("home:homepage")
    return render(request, 'authentication/register.html', {'form': userForm})


def login(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user and user.is_active:
            login_session(request, user)
            return redirect('home:homepage')
        error_message = django_apps.get_app_config(
            'authentication').INVALID_CREDENTIALS_MESSAGE
    return render(request, 'authentication/login.html', {"error_message": error_message})


@login_required()
def logout(request):
    logout_session(request)
    return redirect('home:homepage')
