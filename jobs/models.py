from django.db import models
from users.models import Company


class Job(models.Model):
    FIELDS_CHOICES = (
        ('P', 'Programmer'),
        ('T', 'Tailor'),
        ('M', 'Mechanical Engineer'),
        ('O', 'Other')
    )
    owner_company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Job-Image/')
    expire_date = models.DateField()
    field = models.CharField(choices=FIELDS_CHOICES, max_length=1)
    salary = models.IntegerField(default=0)
    working_hours = models.IntegerField()
