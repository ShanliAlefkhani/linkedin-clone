from rest_framework import generics, status, permissions
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from users.models import Person, Company, User
from users.serializers import PersonSerializer, CompanySerializer, PersonUpdateSerializer, CompanyUpdateSerializer


class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonUpdateSerializer


class CompanyList(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class PersonSignUp(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = PersonSerializer


class CompanySignUp(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = CompanySerializer


class ProfileUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()

    def get_object(self):
        try:
            Person.objects.get(user=self.request.user)
            return self.request.user.person
        except:
            return self.request.user.company

    def get_serializer_class(self):
        try:
            Person.objects.get(user=self.request.user)
            return PersonUpdateSerializer
        except:
            return CompanyUpdateSerializer
