from rest_framework import serializers
from jobs.models import Job, Application
from users.serializers import CompanySerializer, PersonSerializer


class JobSerializer(serializers.ModelSerializer):
    company = serializers.SerializerMethodField()

    class Meta:
        model = Job
        fields = ('company', 'title', 'image', 'expire_date', 'field', 'salary', 'working_hours')

    def create(self, validated_data):
        job, created = Job.objects.update_or_create(company=self.context['request'].user.company,
                                                    title=validated_data.get('title'),
                                                    image=validated_data.get('image'),
                                                    expire_date=validated_data.get('expire_date'),
                                                    field=validated_data.get('field'),
                                                    salary=validated_data.get('salary'),
                                                    working_hours=validated_data.get('working_hours'))
        return job

    def get_company(self, obj):
        company = CompanySerializer(obj.company).data
        company.pop('user')
        return company


class JobUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('title', 'image', 'expire_date', 'field', 'salary', 'working_hours')


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('job',)


class ApplicationListSerializer(serializers.ModelSerializer):
    job = serializers.SerializerMethodField(read_only=True)
    person = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Application
        fields = ('job', 'person')

    def get_person(self, obj):
        person = PersonSerializer(obj.person).data
        person.pop('user')
        return person

    def get_job(self, obj):
        job = JobSerializer(obj.job).data
        job.pop('company')
        return job
