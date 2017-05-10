from django.views.generic import ListView
from .models import Page

class PageList (ListView):
    model = Page
