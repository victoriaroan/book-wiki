from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^markdownx/', include('markdownx.urls')),
    url(r'^admin/', admin.site.urls),

    url(r'^', include('bookwiki.core.urls')),
    url(r'^', include('bookwiki.projects.urls')),
    url(r'^', include('bookwiki.books.urls')),
]
