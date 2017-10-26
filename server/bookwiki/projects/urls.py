from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    url(r'^create/$', login_required(views.ProjectCreateView.as_view()), name='project-create'),
]
