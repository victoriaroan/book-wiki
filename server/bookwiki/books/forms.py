from bootstrap import widgets
from django import forms

from . import models
from bookwiki.core.widgets import BootstrapMdxWidget

class PageForm (forms.ModelForm):
    class Meta:
        model = models.Page
        fields = ('book', 'title', 'content',)
        widgets = widgets.ModelWidgets(models.Page, overrides={
            'content': BootstrapMdxWidget
        })
