from django.db import models
from django.conf import settings

# Create your models here.

SHORTCODE_MAX = getattr(settings, 'SHORTCODE_MAX', 15)

class ShortURL(models.Model):
    url = models.CharField(max_length=256)
    shortcode = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True, null=True)
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)