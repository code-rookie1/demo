from django.urls import path, re_path
from req.views import StudentsGenericAPIView, StudentGenericAPIView, Students2GenericAPIView, Student2GenericAPIView

urlpatterns = [

    # re_path(r'^reqs/(?P<pk>\d+)/$', StudentsGenericAPIView.as_view(), name='reqs'),
    re_path(r'^req/(?P<pk>\d+)/', StudentGenericAPIView.as_view()),
    # re_path(r'^reqs2/(?P<pk>\d+)/$', Students2GenericAPIView.as_view(), name='reqs2'),
    # re_path(r'^req2/(?P<pk>\d+)/$', Student2GenericAPIView.as_view(), name='req2'),

]
