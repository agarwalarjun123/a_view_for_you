from django.apps import AppConfig


class AuthenticationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    type = {'GOOGLE_LOGIN': 'GOOGLE_LOGIN', 'PASSWORD_LOGIN':'PASSWORD_LOGIN'}
    name = 'authentication'
    INVALID_CREDENTIALS_MESSAGE = "Invalid Credentials Provided."
