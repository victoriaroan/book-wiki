from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect
from django.views.generic import CreateView, DetailView, UpdateView

from bookwiki.core.generic import LayoutMixin, LayoutTemplates, LayoutView

from . import models
from .forms import ProjectForm, PageForm

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

#     def form_valid(self, form):
#         self.object = form.save()
#         # Create the default index page.
#         self.object.index_page = models.Page.objects.create(
#             title='Welcome to book-wiki!',
#             project=self.object,
#             content="**This is your project's index page.** You can edit it by clicking on the edit button in the top right. You can change what shows up on your project dashboard by editing the project settings."
#         )
#         self.object.save()
#         return redirect(self.get_success_url())

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


class PageCreateView (PermissionRequiredMixin, LayoutMixin, CreateView):
    model = models.Page
    form_class = PageForm
    slug_field = 'slug'
    slug_url_kwarg = 'page'
    permission_required = 'books.can_create_page'

    def get_form_kwargs(self):
        kwargs = super(PageCreateView, self).get_form_kwargs()

        # Pass in the project and book to the form.
        kwargs['project'] = self.request.project
        kwargs['book'] = self.request.book
        return kwargs

#     def form_valid(self, form):
#         """
#         If the form is valid, add project and save the associated model.
#         """
#         self.object = form.save(commit=False)
#         self.object.project = self.request.project
#         self.object.save()
#         return redirect(self.get_success_url())

class PageEditView (PermissionRequiredMixin, LayoutMixin, UpdateView):
    template_name_suffix = '_edit'
    model = models.Page
    form_class = PageForm
    slug_field = 'id'
    slug_url_kwarg = 'slug'
    permission_required = 'books.can_edit_page'

class PageDetailView (PermissionRequiredMixin, LayoutMixin, DetailView):
    model = models.Page
    slug_field = 'id'
    slug_url_kwarg = 'slug'
    permission_required = 'projects.can_view'
