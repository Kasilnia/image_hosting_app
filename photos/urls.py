from django.conf.urls import url

from .views import (HomepageView, PhotoCreateView, PhotoDeleteView,
                    PhotoDetailView)


urlpatterns = [
    url(r'^detail/(?P<pk>\d+)/(?P<slug>[\w\d_-]+)/$',
        PhotoDetailView.as_view(),
        name='detail_photo'),
    url(r'^create/$', PhotoCreateView.as_view(), name='create_photo'),
    url(r'^delete/(?P<pk>\d+)/$',
        PhotoDeleteView.as_view(),
        name='delete_photo'),
    url(r'^$', HomepageView.as_view(), name='homepage'),
]
