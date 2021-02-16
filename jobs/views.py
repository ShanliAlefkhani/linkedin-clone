from django.utils import timezone
from rest_framework import generics, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from jobs.bstFilter import SalaryFilter
from jobs.models import Job, Application
from jobs.serializers import JobSerializer, ApplicationSerializer, ApplicationListSerializer, JobUpdateSerializer
from users.permissions import IsCompany, IsOwner


class JobList(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SalaryFilter]
    ordering_fields = ['expire_date', 'salary', 'working_hours']
    search_fields = ['title']
    authentication_classes = [TokenAuthentication]


class JobCreate(generics.CreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated, IsCompany]
    authentication_classes = [TokenAuthentication]


class JobUpdate(generics.RetrieveUpdateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobUpdateSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    authentication_classes = [TokenAuthentication]


class Apply(generics.CreateAPIView):
    queryset = Job.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def post(self, request, *args, **kwargs):
        job = Job.objects.get(pk=request.data['job'])
        if timezone.now().date() < job.expire_date:
            submit, created = Application.objects.get_or_create(person=request.user.person, job=job)
            submit.save()
            return Response("Your Application Added Successfully", status=status.HTTP_200_OK)
        return Response("Job was expired", status=status.HTTP_400_BAD_REQUEST)


class ApplicationList(generics.ListAPIView):
    serializer_class = ApplicationListSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        return Application.objects.filter(job__company=self.request.user.company)
