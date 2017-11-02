from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import CreateView, DetailView, View
from django.views.generic.base import ContextMixin

from bookwiki.core.generic import LayoutMixin, LayoutTemplates

from .forms import ProjectForm
from . import models

class ProjectView (ContextMixin, View):
    """
    A project-based context view that automatically gets the project slug from
    the url, retrieves the related project, stores it in the request, and puts
    the project in the context data. Requires the project slug to be in a "pid"
    urlconf parameter.
    """
    def dispatch(self, request, *args, **kwargs):
        # This will raise a 404 if the project doesn't exist or the url doesn't have a pid.
        request.project = models.Project.objects.get(slug=kwargs.get('pid', None))
        return View.dispatch(self, request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = ContextMixin.get_context_data(self, **kwargs)
        context.update({
            'project': self.request.project,
        })
        return context

class ProjectCreateView (PermissionRequiredMixin, LayoutMixin, CreateView):
    layout_template = LayoutTemplates.FULL_PANE
    model = models.Project
    slug_field = 'slug'
    slug_url_kwarg = 'pid'
    permission_required = 'projects.can_create'
    form_class = ProjectForm

#     def has_permission(self):
#         can_edit = PermissionRequiredMixin.has_permission(self)
#         return can_edit or self.request.user.pk == self.get_object()

class ProjectDetailView (PermissionRequiredMixin, LayoutMixin, DetailView):
    model = models.Project
    slug_field = 'slug'
    slug_url_kwarg = 'pid'
    permission_required = 'projects.can_view'

class ProjectDashboardView (LayoutMixin, ProjectView):
    model = models.Project
    slug_field = 'slug'
    slug_url_kwarg = 'pid'
    template_name = 'projects/dashboard.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render(context)
