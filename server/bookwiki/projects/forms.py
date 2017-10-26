from bootstrap import widgets
from django import forms
from . import models

class ProjectForm (forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ('name', 'slug', 'description',)
        widgets = widgets.ModelWidgets(models.Project)
