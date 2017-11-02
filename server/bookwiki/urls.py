from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^mdx/', include('markdownx.urls')),
    url(r'^admin/', admin.site.urls),

    url(r'^', include('bookwiki.core.urls')),
    url(r'^books/', include('bookwiki.books.urls')),
    url(r'^', include('bookwiki.projects.urls')),
]
