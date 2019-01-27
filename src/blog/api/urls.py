from django.conf.urls import url
from .views import PostListCreateAPIVIEW


urlpatterns = [
    url(r'^$', PostListCreateAPIVIEW.as_view())
]