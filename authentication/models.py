from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.apps import apps as django_apps
from django.contrib.auth.signals import user_logged_in
from allauth.socialaccount.models import SocialAccount

class Manager(BaseUserManager):
    def create_user(self, email, username, password, type, **kwargs):
        if not email:
            raise ValueError('User must have a email address')
        user = self.model(email=self.normalize_email(
            email), username=username, type=type, **kwargs)
        if type == django_apps.get_app_config('authentication').type['PASSWORD_LOGIN']:
            if not password:
                raise ValueError('User must have a password field')
            user.save()
            user.set_password(password)
        else:
            user.save()
        
        return user

    def create_superuser(self, email, username, password, **kwargs):
        user = self.create_user(
            email,
            username=username,
            password=password,
            type=django_apps.get_app_config('authentication').type['PASSWORD_LOGIN'], **kwargs)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class User(AbstractUser):
    profile_image = models.FileField(upload_to='media/', blank=True)
    type = models.CharField(max_length=50, choices=django_apps.get_app_config(
        'authentication').type.items())
    username = models.CharField(max_length=200)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = Manager()
    class Meta:
        unique_together = ('email',)

def login_handler(sender, user, request, **kwargs):
    account = None
    try:
        account = SocialAccount.objects.get(user = request.user)
    except:
        return
    user_data = account.extra_data
    user.profile_image = user_data['picture']
    user.type = django_apps.get_app_config('authentication').type['GOOGLE_LOGIN']
    user.save()
    

user_logged_in.connect(login_handler)