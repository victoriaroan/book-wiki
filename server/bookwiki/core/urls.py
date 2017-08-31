from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^login/$', views.CoreLoginView.as_view(), name='login'),
    url(r'^logout/$', views.CoreLogoutView.as_view(), name='logout'),
    url(r'^profile/(?P<username>\w+)/$', login_required(views.ProfileView.as_view()), name='profile-view'),
    url(r'^profile/(?P<username>\w+)/edit/$', login_required(views.ProfileEditView.as_view()), name='profile-edit'),
]
