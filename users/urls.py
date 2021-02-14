from django.urls import path, include
from users import views
from users.views import SignUpPerson, SignUpCompany, UpdateProfile

urlpatterns = [
    path('list-person/', views.PersonList.as_view()),
    path('list-company/', views.CompanyList.as_view()),
    path('signup-person/', SignUpPerson.as_view()),
    path('signup-company/', SignUpCompany.as_view()),
    path('update-profile/', UpdateProfile.as_view()),
    path('', include('rest_framework.urls')),
]
