from base64 import encode
from django.utils.timezone import now
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
    address = models.TextField()
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='landscapes')
    activities = models.JSONField(default=list, blank = True)
    accessibilities = models.JSONField(default=list, blank = True)
    is_active = models.BooleanField(default=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=6)
    longitude = models.DecimalField(max_digits=10, decimal_places=6)
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Landscape,self).save(*args, **kwargs)

class Review(Base):
    TITLE_MAX_LENGTH = 500
    MULTIPLECHOICE_MAX_LENGTH = 500
    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    description = models.TextField(blank=True)
    rating = models.FloatField(null=False, blank=True, default=5)
    visit_date = models.DateTimeField(default=now, blank=True)
    facilities = models.CharField(max_length = MULTIPLECHOICE_MAX_LENGTH)
    activities = models.CharField(max_length = MULTIPLECHOICE_MAX_LENGTH)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    landscape_id = models.ForeignKey(Landscape, on_delete = models.CASCADE)

    def __str__(self):
        return self.title

class Photo(Base):
    review_id = models.ForeignKey(Review, on_delete = models.CASCADE, null=True)
    landscape_id = models.ForeignKey(Landscape, on_delete = models.CASCADE, null=True)
    image = models.ImageField(upload_to='landscapes', null=True, blank=True)

class saved_landscapes (models.Model):
    user_id = models.ForeignKey(Review, on_delete = models.CASCADE, null=True)
    landscape_id = models.ForeignKey(Landscape, on_delete = models.CASCADE, null=True)

class Like(Base):
    date = models.DateTimeField(default=now, blank=True)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    landscape_id = models.ForeignKey(Landscape, on_delete = models.CASCADE)