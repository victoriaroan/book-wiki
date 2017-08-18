from django.contrib.auth.views import LoginView, LogoutView

from bookwiki.core.generic import LayoutView, LayoutMixin

class HomeView (LayoutView):
    template_name = 'core/index.html'

class CoreLoginView (LayoutMixin, LoginView):
    pass

class CoreLogoutView (LayoutMixin, LogoutView):
    pass
