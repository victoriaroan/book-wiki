from django.contrib.auth import get_user_model, get_user
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import DetailView, UpdateView

from bookwiki.core.generic import LayoutView, LayoutMixin
from django.contrib.auth.mixins import PermissionRequiredMixin

class HomeView (LayoutView):
    template_name = 'core/index.html'

class CoreLoginView (LayoutMixin, LoginView):
    pass

class CoreLogoutView (LayoutMixin, LogoutView):
    pass

class ProfileView (LayoutMixin, DetailView):
    model = get_user_model()
    slug_field = 'username'
    slug_url_kwarg = 'username'

class ProfileEditView (PermissionRequiredMixin, LayoutMixin, UpdateView):
    model = get_user_model()
    slug_field = 'username'
    slug_url_kwarg = 'username'
    fields = ['first_name', 'last_name', 'email']
    permission_required = 'users.can_edit'
    
    def has_permission(self):
        can_edit = PermissionRequiredMixin.has_permission(self)
        print(self.request.user)
        print(self.get_object())
        return can_edit or self.request.user.pk == self.get_object()
    
