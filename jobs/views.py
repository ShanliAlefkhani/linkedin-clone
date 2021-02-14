from django.utils import timezone
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from jobs.models import Job, Application
from jobs.serializers import JobSerializer, JobUpdateSerializer, ApplicationSerializer
from users.permissions import IsCompany, IsOwner


class JobList(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]


class JobCreate(generics.CreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated, IsCompany]

    def post(self, request, *args, **kwargs):
        serializer = JobSerializer(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


class JobUpdate(generics.RetrieveUpdateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_object(self):
        return self.request.user.company

    def get_serializer_class(self):
        return JobUpdateSerializer


class Apply(generics.CreateAPIView):
    queryset = Job.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        job = Job.objects.get(pk=request.data['job'])
        if timezone.now().date() < job.expire_date:
            submit, created = Application.objects.get_or_create(person=request.user.person, job=job)
            submit.save()
            return Response("Your Application Added Successfully", status=status.HTTP_200_OK)
        return Response("Job was expired", status=status.HTTP_400_BAD_REQUEST)
