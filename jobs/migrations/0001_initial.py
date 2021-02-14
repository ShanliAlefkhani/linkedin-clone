# Generated by Django 3.1.6 on 2021-02-14 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='Job-Image/')),
                ('expire_date', models.DateField()),
                ('field', models.CharField(choices=[('P', 'Programmer'), ('T', 'Tailor'), ('M', 'Mechanical Engineer'), ('O', 'Other')], max_length=1)),
                ('salary', models.IntegerField(default=0)),
                ('working_hours', models.IntegerField()),
                ('owner_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.company')),
            ],
        ),
    ]
