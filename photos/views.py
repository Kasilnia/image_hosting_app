from django.views.generic import ListView

from .models import Photo


class HomepageView(ListView):
    """HomepageView displays photos list and menu."""
    model = Photo
    template_name = 'photos/homepage.html'
