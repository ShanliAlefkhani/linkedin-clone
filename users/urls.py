from django.urls import path, include
from users import views
from users.views import PersonSignUp, CompanySignUp, ProfileUpdate, Login

urlpatterns = [
    path('person-list/', views.PersonList.as_view()),
    path('company-list/', views.CompanyList.as_view()),
    path('person-signup/', PersonSignUp.as_view()),
    path('company-signup/', CompanySignUp.as_view()),
    path('accounts/profile/', ProfileUpdate.as_view()),
    path('login/', Login.as_view()),
]
