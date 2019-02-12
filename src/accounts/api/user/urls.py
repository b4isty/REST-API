from django.conf.urls import url, include
from accounts.api.user.views import UserDetailApiView, UserStatusAPIView

urlpatterns = [
    url(r'^(?P<username>\w+)/$', UserDetailApiView.as_view(), name='detail'),
    url(r'^(?P<username>\w+)/status/$', UserStatusAPIView.as_view(), name='status-list')
]