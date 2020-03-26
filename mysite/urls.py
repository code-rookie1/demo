from django.urls import path
from mysite.views import UserInfoView

urlpatterns = [

    path('mysite/', UserInfoView.as_view())
]
