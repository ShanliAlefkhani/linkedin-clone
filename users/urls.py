from django.urls import path
from users import views

urlpatterns = [
    path('person-list/', views.PersonList.as_view()),
    path('company-list/', views.CompanyList.as_view()),
]
