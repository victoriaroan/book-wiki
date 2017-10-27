from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import CreateView, DetailView
from bookwiki.core.generic import LayoutMixin, LayoutTemplates
from .forms import ProjectForm
from . import models

class ProjectCreateView (PermissionRequiredMixin, LayoutMixin, CreateView):
    layout_template = LayoutTemplates.FULL_PANE
    model = models.Project
    slug_field = 'slug'
    slug_url_kwarg = 'project'
    permission_required = 'projects.can_create'
    form_class = ProjectForm

#     def has_permission(self):
#         can_edit = PermissionRequiredMixin.has_permission(self)
#         return can_edit or self.request.user.pk == self.get_object()

class ProjectDetailView (PermissionRequiredMixin, LayoutMixin, DetailView):
    model = models.Project
    slug_field = 'slug'
    slug_url_kwarg = 'project'

