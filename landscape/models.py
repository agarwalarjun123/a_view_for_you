from django.db import models
from django.core.validators import RegexValidator
from slugify import slugify
import json
from utils.utils import Base
# Create your models here.
class Landscape(Base):
    name = models.CharField(max_length=200, validators=[
                            RegexValidator('^[A-Za-z0-9 ]+$')])
    description = models.TextField()
    address = models.TextField(blank=True)
    slug = models.SlugField()
    images = models.TextField(blank=True)
    activities = models.JSONField(default=json.dumps([]))
    accessibilities = models.JSONField(default=json.dumps([]))
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
