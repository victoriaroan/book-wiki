from . import models

class ProjectMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Before view
        response = self.get_response(request)
        # After view
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        # Try to get psn from url and set request.project.
        psn = view_kwargs.get('psn', None)
        request.project = models.Project.objects.get(psn=psn) if psn else None

        # Try to get bsn from url and set request.book.
        bsn = view_kwargs.get('bsn', None)
        request.book = models.Book.objects.get(bsn=bsn) if bsn else None
