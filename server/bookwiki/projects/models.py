from django.db import models
from django.urls.base import reverse

class Project (models.Model):
    psn = models.CharField('Short Name', max_length=15, blank=False, help_text='Used as the slug in URLs.')
    name = models.CharField(max_length=250)
    description = models.TextField(null=False, blank=True)
    index_page = models.ForeignKey('books.Page', models.PROTECT, related_name='+', null=True)

    protected = models.BooleanField(editable=False, default=False)

    def get_absolute_url(self):
        return reverse('project-detail', args=[self.slug])
