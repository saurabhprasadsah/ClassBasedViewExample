# Generated by Django 4.2.3 on 2023-09-08 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_employee_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(max_length=30),
        ),
    ]
