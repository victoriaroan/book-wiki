from django.db import models

class Project (models.Model):
    name = models.CharField(max_length=250)
    slug = models.CharField(max_length=15)
    
    protected = models.BooleanField(editable=False, default=False)