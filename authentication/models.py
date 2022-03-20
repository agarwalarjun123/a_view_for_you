from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.apps import apps as django_apps
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from allauth.socialaccount.models import SocialAccount
from allauth.socialaccount.signals import pre_social_login
from django.shortcuts import redirect
from utils.utils import read_image_from_url
from allauth.exceptions import ImmediateHttpResponse

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
    profile_image = models.ImageField(upload_to='profile_images', blank=True)
    type = models.CharField(max_length=50, choices=django_apps.get_app_config(
        'authentication').type.items(), default = django_apps.get_app_config(
        'authentication').type['PASSWORD_LOGIN'] )
    username = models.CharField(max_length=200)
    introduction = models.CharField(max_length=400, blank=True)
    USERNAME_FIELD = 'email'
    def image_url(self):
        if self.profile_image and hasattr(self.profile_image, 'url'):
            return self.profile_image.url
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
    file,name = read_image_from_url(user_data['picture'])
    user.profile_image.save(name,file)
    user.type = django_apps.get_app_config('authentication').type['GOOGLE_LOGIN']
    user.save()

@receiver(pre_social_login)
def link_to_local_user(sender, request, sociallogin, **kwargs):
    email_address = sociallogin.account.extra_data['email']
    print(email_address)
    users = User.objects.filter(email = email_address)
    if len(users) > 0 and users[0].type == django_apps.get_app_config('authentication').type['PASSWORD_LOGIN']:
        raise ImmediateHttpResponse(redirect('auth:login'))


user_logged_in.connect(login_handler)