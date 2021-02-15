from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.exceptions import NotAuthenticated

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
            user = UserSerializer.create(UserSerializer(), validated_data={'username': username, 'password': password})
            person, created = Person.objects.update_or_create(user=user,
                                                              name=validated_data.get('name'),
                                                              surname=validated_data.get('surname'),
                                                              birthday=validated_data.get('birthday'),
                                                              gender=validated_data.get('gender'))
            return person


class PersonUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['name', 'surname', 'birthday', 'gender', 'field', 'resume']


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
            user = UserSerializer.create(UserSerializer(), validated_data={'username': username, 'password': password})
            company, created = Company.objects.update_or_create(user=user,
                                                                name=validated_data.get('name'),
                                                                creation_date=validated_data.get('creation_date'),
                                                                address=validated_data.get('address'),
                                                                telephone_number=validated_data.get('telephone_number'))
            return company


class CompanyUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name', 'creation_date', 'address', 'telephone_number', 'field']


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100, write_only=True)

    def validate(self, attrs):
        username = attrs.get("username", None)
        password = attrs.get("password", None)
        user = authenticate(username=username, password=password)
        if user is None:
            raise NotAuthenticated('This user does not exist.')
        return UserSerializer(instance=user).data

    def to_representation(self, instance):
        return instance
