from markdownx.widgets import MarkdownxWidget

class BootstrapMdxWidget (MarkdownxWidget):
    template_name = 'forms/bootstrapmdx.html'

    def __init__(self, attrs=None):
        default_attrs = {'class': 'form-control'}
        if attrs:
            default_attrs.update(attrs)
        super(BootstrapMdxWidget, self).__init__(default_attrs)

    def get_context(self, name, value, attrs=None):
        # Have to update the attrs with self.attrs here because MarkdownxWidget overwrites the class.
        attrs.update(self.attrs)
        return MarkdownxWidget.get_context(self, name, value, attrs=attrs)
