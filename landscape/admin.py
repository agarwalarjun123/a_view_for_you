from django.contrib import admin
from .models import Landscape, Photo, Review
# Register your models here.
class LandscapeAdmin(admin.ModelAdmin):
        prepopulated_fields = {"slug": ("name",)}
        readonly_fields = ('created_at','updated_at')

admin.site.register(Landscape,LandscapeAdmin)
admin.site.register(Review)
admin.site.register(Photo)