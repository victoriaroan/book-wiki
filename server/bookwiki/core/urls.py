from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^login/$', views.CoreLoginView.as_view(), name='login'),
    url(r'^logout/$', views.CoreLogoutView.as_view(), name='logout'),
]
