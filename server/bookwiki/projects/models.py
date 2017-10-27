from django.db import models
from django.urls.base import reverse

class Project (models.Model):
    name = models.CharField(max_length=250)
    slug = models.CharField(max_length=15, blank=False)
    description = models.TextField(null=False, blank=True)

    protected = models.BooleanField(editable=False, default=False)

    def get_absolute_url(self):
        return reverse('project-detail', args=[self.slug])
