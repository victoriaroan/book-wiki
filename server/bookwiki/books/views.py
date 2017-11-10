from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http.response import HttpResponseRedirect
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView

from bookwiki.core.generic import LayoutMixin

from . import models
from .forms import PageForm

class PageCreateView (PermissionRequiredMixin, LayoutMixin, CreateView):
    model = models.Page
    form_class = PageForm
    slug_field = 'slug'
    slug_url_kwarg = 'page'
    permission_required = 'books.can_create_page'

    def form_valid(self, form):
        """
        If the form is valid, add project and save the associated model.
        """
        self.object = form.save(commit=False)
        self.object.project = self.request.project
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class PageEditView (PermissionRequiredMixin, LayoutMixin, UpdateView):
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
