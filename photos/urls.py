from django.conf.urls import url

from .views import HomepageView, PhotoCreateView


urlpatterns = [
    url(r'^create/$', PhotoCreateView.as_view(), name='create_photo'),
    url(r'^$', HomepageView.as_view(), name='homepage'),
]
