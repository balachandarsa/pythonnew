# Generated by Django 5.0.1 on 2024-01-29 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.IntegerField()),
                ('emp_name', models.CharField(max_length=23)),
                ('emp_phone', models.IntegerField()),
                ('emp_address', models.CharField(max_length=20)),
                ('emp_email', models.EmailField(max_length=254)),
                ('emp_salary', models.IntegerField()),
            ],
        ),
    ]