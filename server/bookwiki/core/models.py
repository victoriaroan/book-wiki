from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class TrackedModel(models.Model):
    # Will probably eventually replace this with model history/reversion app.
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.PROTECT)

    class Meta:
        abstract = True

class User(AbstractUser):
    protected = models.BooleanField(editable=False, default=False)
