from base64 import encode
from django.db import models
from django.core.validators import RegexValidator
from slugify import slugify
from authentication.models import User
from utils.utils import Base
from django.apps import apps
# Create your models here.
class Landscape(Base):
    
    name = models.CharField(max_length=apps.get_app_config('landscape').landscape_max_length, validators=[
                            RegexValidator('^[A-Za-z0-9 ]+$')])
    description = models.TextField()
    address = models.TextField(blank=True)
    slug = models.SlugField()
    images = models.TextField(blank=True)
    activities = models.JSONField(default=list)
    accessibilities = models.JSONField(default=list)
    is_active = models.BooleanField(default=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=6)
    longitude = models.DecimalField(max_digits=10, decimal_places=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Landscape,self).save(*args, **kwargs)

class Review(Base):
    TITLE_MAX_LENGTH = 500
    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    description = models.TextField(blank=True)
    rating = models.IntegerField
    visit_date = models.DateTimeField(auto_now_add=True)
    images = models.TextField(blank=True)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    landscape_id = models.ForeignKey(Landscape, on_delete = models.CASCADE)

    def __str__(self):
        return self.title
