from bootstrap import widgets
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from bookwiki.projects import models

class ProjectForm (forms.ModelForm):
    def clean(self):
        # TODO: verify PSN against a blacklist of URLs that they would conflict with.
        return super(ProjectForm, self).clean()

    def save(self, commit=True):
        # If we're creating a new project, create a default index page.
        # TODO: this doesn't work.
        if not self.instance.pk:
            self.instance.index_page = models.Page.objects.create(
                title='Welcome to book-wiki!',
                project=self.instance,
                content="**This is your project's index page.** You can edit it by clicking on the edit button in the top right. You can change what shows up on your project dashboard by editing the project settings."
            )
        return super(ProjectForm, self).create(commit)

    class Meta:
        model = models.Project
        fields = ('psn', 'name', 'description',)
        widgets = widgets.ModelWidgets(models.Project)

class PageForm (forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.project = kwargs.pop('project', None)
        super(PageForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(PageForm, self).clean()

        # Make sure a project is defined. We should never actually get to this
        # point, but ya never know...
        if self.project is None:
            raise ValidationError(_('All pages must be associated with a project.'), code='required')
        return cleaned_data

    def save(self, commit=True):
        self.instance.project = self.project
        return super(PageForm, self).save(commit)

    class Meta:
        model = models.Page
        fields = ('title', 'content',)
        widgets = widgets.ModelWidgets(models.Page)
