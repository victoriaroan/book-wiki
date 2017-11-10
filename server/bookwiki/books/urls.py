from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    url(r'^(?P<psn>[\w\-]+)/add-page/$', login_required(views.PageCreateView.as_view()), name='page-create'),
    url(r'^(?P<psn>[\w\-]+)/(?P<slug>[\w\-]+)/$', login_required(views.PageDetailView.as_view()), name='page-detail'),
    url(r'^(?P<psn>[\w\-]+)/(?P<slug>[\w\-]+)/edit/$', login_required(views.PageEditView.as_view()), name='page-edit'),
]
