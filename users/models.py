from django.contrib.auth.models import User
from django.db import models


class Person(models.Model):
    GENDER_CHOICES = (
        ('F', 'Female'),
        ('M', 'Male')
    )
    user = models.OneToOneField(User, related_name='person', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    birthday = models.DateField('birthday')
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1)

    class Meta:
        ordering = ['name']


class Company(models.Model):
    user = models.OneToOneField(User, related_name='company', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    creation_date = models.DateField('creation date')
    address = models.TextField(max_length=200)
    telephone_number = models.PositiveIntegerField()

    class Meta:
        ordering = ['name']
