from django.views.generic import ListView
from django.views.generic.edit import CreateView

from .models import Photo


class HomepageView(ListView):
    """HomepageView displays photos list and menu."""
    model = Photo
    template_name = 'photos/homepage.html'


class PhotoCreateView(CreateView):
    """PhotoCreateView creates new photo object."""
    model = Photo
    fields = ['title', 'image']
    success_url = '/'  # TODO Redirect to details page
