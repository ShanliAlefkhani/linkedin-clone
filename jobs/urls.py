from django.urls import path
from jobs.views import JobList, JobCreate, JobUpdate

urlpatterns = [
    path('jobs/', JobList.as_view()),
    path('jobs-create/', JobCreate.as_view()),
    path('jobs/<pk>/update/', JobUpdate.as_view()),
]
