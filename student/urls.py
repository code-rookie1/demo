from django.urls import path
from student.views import StudentView

urlpatterns = [

    path('student/', StudentView.as_view())
]
