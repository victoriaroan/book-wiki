from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http.response import HttpResponseRedirect
from django.views.generic import CreateView, DetailView

from bookwiki.books import models as book_models
from bookwiki.core.generic import LayoutMixin, LayoutTemplates, LayoutView

from .forms import ProjectForm
from . import models
from django.urls.base import reverse

class ProjectCreateView (PermissionRequiredMixin, LayoutMixin, CreateView):
    layout_template = LayoutTemplates.FULL_PANE
    model = models.Project
    slug_field = 'psn'
    slug_url_kwarg = 'psn'
    permission_required = 'projects.can_create'
    form_class = ProjectForm

#     def has_permission(self):
#         can_edit = PermissionRequiredMixin.has_permission(self)
#         return can_edit or self.request.user.pk == self.get_object()

    def form_valid(self, form):
        self.object = form.save()
        # Create the default index page.
        self.object.index_page = book_models.Page.objects.create(
            title='Welcome to book-wiki!',
            project=self.object,
            content="**This is your project's index page.** You can edit it by clicking on the edit button in the top right. You can change what shows up on your project dashboard by editing the project settings."
        )
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class ProjectDetailView (PermissionRequiredMixin, LayoutMixin, DetailView):
    model = models.Project
    slug_field = 'psn'
    slug_url_kwarg = 'psn'
    permission_required = 'projects.can_view'

class ProjectDashboardView (LayoutView):
    model = models.Project
    slug_field = 'psn'
    slug_url_kwarg = 'psn'
    template_name = 'projects/dashboard.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render(context)
