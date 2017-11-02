from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    url(r'^new-project/$', login_required(views.ProjectCreateView.as_view()), name='project-create'),
    url(r'^(?P<psn>[\w\-]+)/$', login_required(views.ProjectDashboardView.as_view()), name='project-dashboard'),
    url(r'^(?P<psn>[\w\-]+)/detail/$', login_required(views.ProjectDetailView.as_view()), name='project-detail'),
]
