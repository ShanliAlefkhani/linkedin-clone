from django.urls import path
from jobs.views import JobList

urlpatterns = [
    path('jobs/', JobList.as_view()),
]
