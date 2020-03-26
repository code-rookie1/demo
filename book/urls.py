from django.urls import path
from book.views import BookInfoView

urlpatterns = [

    path('book/', BookInfoView.as_view())
]
