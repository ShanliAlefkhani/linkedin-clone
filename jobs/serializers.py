from rest_framework import serializers
from jobs.models import Job


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
