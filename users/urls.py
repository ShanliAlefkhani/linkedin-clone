from django.urls import path
from users import views
from users.views import SignUpPerson, SignUpCompany

urlpatterns = [
    path('list-person/', views.PersonList.as_view()),
    path('list-company/', views.CompanyList.as_view()),
    path('signup-person/', SignUpPerson.as_view()),
    path('signup-company/', SignUpCompany.as_view()),
]
