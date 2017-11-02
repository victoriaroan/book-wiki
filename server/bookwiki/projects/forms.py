from bootstrap import widgets
from django import forms
from . import models

class ProjectForm (forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ('psn', 'name', 'description',)
        widgets = widgets.ModelWidgets(models.Project)
