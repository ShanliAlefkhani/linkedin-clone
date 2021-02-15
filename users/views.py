from rest_framework import generics, status, permissions
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from users.models import Person, Company, User
from users.permissions import IsPerson
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

    def post(self, request, *args, **kwargs):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


class CompanySignUp(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = CompanySerializer

    def post(self, request, *args, **kwargs):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


class ProfileUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()

    def get_object(self):
        if IsPerson:
            return self.request.user.person
        else:
            return self.request.user.company

    def get_serializer_class(self):
        if IsPerson:
            return PersonUpdateSerializer
        else:
            return CompanyUpdateSerializer
