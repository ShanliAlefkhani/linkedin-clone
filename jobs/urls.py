from django.urls import path
from jobs.views import JobList, JobCreate

urlpatterns = [
    path('jobs/', JobList.as_view()),
    path('jobs-create/', JobCreate.as_view()),
]
