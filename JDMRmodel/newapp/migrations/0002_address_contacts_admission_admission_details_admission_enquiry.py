# Generated by Django 3.1.3 on 2021-06-16 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address_Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('School_Address', models.CharField(max_length=50)),
                ('School_Chairman_Principal', models.CharField(max_length=200)),
                ('Phone_Number', models.CharField(max_length=50)),
                ('Email_Address', models.EmailField(max_length=200)),
                ('School_Website', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='admission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classname', models.CharField(max_length=150)),
                ('session', models.CharField(max_length=50)),
                ('last_date', models.DateTimeField()),
                ('Application_Fees', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Admission_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Academic_Year', models.CharField(max_length=100)),
                ('Admission_Period', models.CharField(max_length=100)),
                ('Fee_Details', models.CharField(max_length=500)),
                ('Description', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Admission_Enquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Email_Address', models.EmailField(max_length=200)),
                ('Phone_Number', models.CharField(max_length=50)),
                ('Your_Message', models.TextField(max_length=1000)),
                ('gender', models.CharField(choices=[('Class LKG', 'Class LKG'), ('Class PRE KG', 'Class PRE KG'), ('Class UKG', 'Class UKG'), ('Class I', 'Class I'), ('Class II', 'Class II'), ('Class III', 'Class III'), ('Class IV', 'Class IV'), ('Class V', 'Class V')], max_length=20)),
            ],
        ),
    ]