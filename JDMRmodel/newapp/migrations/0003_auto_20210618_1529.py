# Generated by Django 3.1.3 on 2021-06-18 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0002_address_contacts_admission_admission_details_admission_enquiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='Admission_Period',
            field=models.DateField(),
        ),
    ]