from django.db import models

class Book (models.Model):
    title = models.CharField(max_length=250)
    short_name = models.CharField(max_length=25)
    slug = models.CharField(max_length=15)
    description = models.TextField()
    date_created = models.DateTimeField()
    project = models.ForeignKey('projects.Project', models.PROTECT, default=1)
    

class Page (models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=25)
    date_created = models.DateTimeField()
    book = models.ForeignKey('Book', models.PROTECT, blank=True, null=True)
    project = models.ForeignKey('projects.Project', models.PROTECT, default=1)
    
    @property
    def file_path(self):
        # Page file path is built from project_slug/book_slug/page_slug.md
        return None
