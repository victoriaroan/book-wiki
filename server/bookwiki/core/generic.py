from __future__ import unicode_literals

from django.views.generic import View
from django.views.generic.base import TemplateResponseMixin, ContextMixin

class LayoutTemplates (object):
    FULL_PANE = 'layouts/full.html'
    SPLIT_PANE = 'layouts/split.html'
    LEFT_ASIDE = 'layouts/left_aside.html'
    RIGHT_ASIDE = 'layouts/right_aside.html'

class LayoutMixin (TemplateResponseMixin):
    base_template = 'base.html'
    layout_template = LayoutTemplates.FULL_PANE

    def render_to_response(self, context, **response_kwargs):
        context.update({
            'base_template': self.base_template,
            'layout_template': self.layout_template,
        })
        return TemplateResponseMixin.render_to_response(self, context, **response_kwargs)

    def render(self, context, **response_kwargs):
        return self.render_to_response(context, **response_kwargs)

class LayoutView (LayoutMixin, ContextMixin, View):
    """
    A view that renders a template using one of the layouts from LayoutTemplates.
    """
    def get(self, request, *args, **kwargs):
        print('template', self.layout_template)
        context = self.get_context_data(**kwargs)
        return self.render(context)
