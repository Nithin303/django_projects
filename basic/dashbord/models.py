from django.db import models

# Create your models here.

class Components(models.Model):
    name = models.CharField(max_length=20)
    state = models.BooleanField(default=False)