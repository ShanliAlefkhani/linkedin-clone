from django.contrib.auth import authenticate
from rest_framework import generics, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from users.models import Person, Company, User
from users.serializers import PersonSerializer, CompanySerializer, PersonUpdateSerializer, CompanyUpdateSerializer, \
    LoginSerializer


class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonUpdateSerializer
    authentication_classes = [TokenAuthentication]


class CompanyList(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    authentication_classes = [TokenAuthentication]


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
    authentication_classes = [TokenAuthentication]

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


class Login(generics.CreateAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username, password)
        token, _ = Token.objects.get_or_create(user=user)
        return Response(
            {'token': token},
            status=200
        )
