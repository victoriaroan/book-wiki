from django.db import models

class Page (models.Model):
    title = models.CharField(max_length=200)
    date_created = models.DateTimeField()
    body = models.TextField()
