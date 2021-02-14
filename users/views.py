from rest_framework import generics
from users.models import Person, Company
from users.serializers import PersonSerializer, CompanySerializer


class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class CompanyList(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
