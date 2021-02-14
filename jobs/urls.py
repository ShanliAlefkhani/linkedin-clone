from django.urls import path
from jobs.views import JobList, JobCreate, JobUpdate

urlpatterns = [
    path('job-list/', JobList.as_view()),
    path('job-create/', JobCreate.as_view()),
    path('job-update/<pk>/', JobUpdate.as_view()),
]
