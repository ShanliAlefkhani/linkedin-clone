from rest_framework import serializers
from users.models import User, Person, Company
from django.db import transaction


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class PersonSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    username = serializers.CharField(read_only=True)
    password = serializers.CharField(read_only=True)

    class Meta:
        model = Person
        fields = ['user', 'username', 'password', 'name', 'surname', 'birthday', 'gender']

    def create(self, validated_data):
        with transaction.atomic():
            username = validated_data['user.username']
            password = validated_data['user.password']
            user_data = {'username': username, 'password': password}
            user = UserSerializer.create(UserSerializer(), validated_data=user_data)
            person, created = Person.objects.update_or_create(user=user, name=validated_data.get('name'),
                                                              surname=validated_data.get('surname'),
                                                              birthday=validated_data.get('birthday'),
                                                              gender=validated_data.get('gender'))
            return person


class PersonUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['name', 'surname', 'birthday', 'gender', 'field', 'resume']

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.surname = validated_data.get('surname', instance.surname)
        instance.birthday = validated_data.get('birthday', instance.birthday)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.field = validated_data.get('field', instance.field)
        instance.resume = validated_data.get('resume', instance.resume)
        instance.save()
        return instance


class CompanySerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    username = serializers.CharField(read_only=True)
    password = serializers.CharField(read_only=True)

    class Meta:
        model = Company
        fields = ['user', 'username', 'password', 'name', 'creation_date', 'address', 'telephone_number']

    def create(self, validated_data):
        with transaction.atomic():
            username = validated_data['user.username']
            password = validated_data['user.password']
            user_data = {'username': username, 'password': password}
            user = UserSerializer.create(UserSerializer(), validated_data=user_data)
            company, created = Company.objects.update_or_create(user=user, name=validated_data.get('name'),
                                                                creation_date=validated_data.get('creation_date'),
                                                                address=validated_data.get('address'),
                                                                telephone_number=validated_data.get('telephone_number'))
            return company


class CompanyUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name', 'creation_date', 'address', 'telephone_number', 'field']

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.creation_date = validated_data.get('creation_date', instance.creation_date)
        instance.address = validated_data.get('address', instance.address)
        instance.telephone_number = validated_data.get('telephone_number', instance.telephone_number)
        instance.field = validated_data.get('field', instance.field)
        instance.save()
        return instance
