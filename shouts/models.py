from django.db import models

# Create your models here.
class Shout(models.Model):
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=30)
