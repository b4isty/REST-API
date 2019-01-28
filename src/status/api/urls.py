from django.conf.urls import url
from .views import StatusListSearchAPIView, StatusAPIView

urlpatterns = [
    url(r'^$', StatusAPIView.as_view()),
    # url(r'^$', StatusListSearchAPIView.as_view()),
    # url(r'^create/$', StatusCreateAPIView.as_view()),
    # url(r'^(?P<id>.*)/$', StatusDetailAPIView.as_view()),
    # url(r'^(?P<id>.*)/update/$', StatusUpdateAPIView.as_view()),
    # url(r'^(?P<id>.*)/delete/$', StatusDeleteAPIView.as_view()),

]