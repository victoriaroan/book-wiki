from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import DetailView, UpdateView
from django.views.generic.list import ListView

from bookwiki.core.generic import LayoutMixin, LayoutTemplates
from bookwiki.projects.models import Project
from .forms import ProfileForm, LoginForm


class HomeView (LayoutMixin, ListView):
    template_name = 'core/index.html'
    model = Project

class CoreLoginView (LayoutMixin, LoginView):
    layout_template = LayoutTemplates.CENTER_PANE
    form_class = LoginForm

class CoreLogoutView (LayoutMixin, LogoutView):
    pass

class ProfileView (LayoutMixin, DetailView):
    layout_template = LayoutTemplates.LEFT_ASIDE
    model = get_user_model()
    slug_field = 'username'
    slug_url_kwarg = 'username'

class ProfileEditView (PermissionRequiredMixin, LayoutMixin, UpdateView):
    layout_template = LayoutTemplates.LEFT_ASIDE
    model = get_user_model()
    slug_field = 'username'
    slug_url_kwarg = 'username'
    permission_required = 'users.can_edit'
    form_class = ProfileForm

    def has_permission(self):
        can_edit = PermissionRequiredMixin.has_permission(self)
        return can_edit or self.request.user.pk == self.get_object()

