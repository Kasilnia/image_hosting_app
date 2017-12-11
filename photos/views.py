from django.views.generic import ListView, DeleteView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

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


class PhotoDeleteView(DeleteView):
    model = Photo
    success_url = reverse_lazy('photos:homepage')
