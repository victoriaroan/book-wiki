from bootstrap import widgets
from django import forms

from . import models

class PageForm (forms.ModelForm):
    class Meta:
        model = models.Page
        fields = ('book', 'title', 'content',)
        widgets = widgets.ModelWidgets(models.Page)
