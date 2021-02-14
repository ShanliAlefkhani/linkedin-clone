from rest_framework import serializers
from jobs.models import Job, Application
from users.serializers import CompanySerializer


class JobSerializer(serializers.ModelSerializer):
    owner_company = serializers.SerializerMethodField()

    class Meta:
        model = Job
        fields = ('owner_company', 'title', 'image', 'expire_date', 'field', 'salary', 'working_hours')

    def create(self, validated_data):
        job, created = Job.objects.update_or_create(owner_company=self.context['request'].user.company,
                                                    title=validated_data.get('title'),
                                                    image=validated_data.get('image'),
                                                    expire_date=validated_data.get('expire_date'),
                                                    field=validated_data.get('field'),
                                                    salary=validated_data.get('salary'),
                                                    working_hours=validated_data.get('working_hours'))
        return job

    def get_owner_company(self, obj):
        owner_company = CompanySerializer(obj.owner_company).data
        owner_company.pop('user')
        return owner_company


class JobUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('title', 'image', 'expire_date', 'field', 'salary', 'working_hours')

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.image = validated_data.get('image', instance.image)
        instance.expire_date = validated_data.get('expire_date', instance.expire_date)
        instance.field = validated_data.get('field', instance.field)
        instance.salary = validated_data.get('salary', instance.salary)
        instance.working_hours = validated_data.get('working_hours', instance.working_hours)
        instance.save()
        return instance


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('job',)
