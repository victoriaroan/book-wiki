from django.db import models
from django.urls.base import reverse
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

from bookwiki.core.models import TrackedModel

class Project (models.Model):
    psn = models.CharField('Short Name', max_length=15, blank=False, unique=True, help_text='Used as the slug in URLs.')
    name = models.CharField(max_length=250)
    description = models.TextField(null=False, blank=True)
    index_page = models.ForeignKey('Page', models.PROTECT, related_name='+', null=True)

    protected = models.BooleanField(editable=False, default=False)

    def get_absolute_url(self):
        return reverse('project-detail', args=[self.psn])

class Book (TrackedModel):
    bsn = models.CharField('Short Name', max_length=25, blank=False)
    title = models.CharField(max_length=250)
    description = models.TextField()
    project = models.ForeignKey('Project', models.PROTECT, blank=False, default=1)

    class Meta:
        unique_together = ('bsn', 'project')

#     def get_absolute_url(self):
#         return reverse('book-index', args=[self.project.psn, self.bsn])

class Page (TrackedModel):
    title = models.CharField(max_length=200)
    project = models.ForeignKey('projects.Project', models.PROTECT, blank=False, default=1)
    # TODO: Make book required and create a "default" book for each project, kinda like the default page?
    book = models.ForeignKey('Book', models.PROTECT, blank=True, null=True)
    content = MarkdownxField(blank=True)

    def clean(self):
        errors = {}
        # If a book is set, it should belong to the page's project.
        if self.book and self.book.project != self.project:
            errors['book'] = _('The book specified does not belong to the same project as the page.')

        if errors:
            raise ValidationError(errors)

    def formatted_content(self):
        return markdownify(self.content)

    @property
    def slug(self):
        """ The slug to use for the page in URLs/filenames. """
        return self.id

    @property
    def file_path(self):
        """ Page file path is built from project_slug/book_slug/page_slug.md """
        return None

    def get_absolute_url(self):
        if self.book:
            return reverse('page-detail', args=[self.project.psn, self.book.bsn, self.page_slug])
        return reverse('page-detail', args=[self.project.psn, self.slug])
