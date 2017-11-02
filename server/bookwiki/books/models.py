from django.db import models
from django.urls.base import reverse

class Book (models.Model):
    bsn = models.CharField('Short Name', max_length=25, blank=False)
    title = models.CharField(max_length=250)
    description = models.TextField()
    date_created = models.DateTimeField()
    project = models.ForeignKey('projects.Project', models.PROTECT, blank=False, default=1)

    class Meta:
        unique_together = ('bsn', 'project')

#     def get_absolute_url(self):
#         return reverse('book-index', args=[self.project.psn, self.bsn])

class Page (models.Model):
    title = models.CharField(max_length=200)
    date_created = models.DateTimeField()
    book = models.ForeignKey('Book', models.PROTECT, blank=True, null=True)
    project = models.ForeignKey('projects.Project', models.PROTECT, blank=False, default=1)

    @property
    def page_slug(self):
        """ The slug to use for the page in URLs/filenames. """
        return

    @property
    def file_path(self):
        """ Page file path is built from project_slug/book_slug/page_slug.md """
        return None

#     def get_absolute_url(self):
#         if self.book:
#             return reverse('page-detail', args=[self.project.psn, self.book.bsn, self.page_slug])
#         return reverse('page-detail', args=[self.project.psn, self.page_slug])
