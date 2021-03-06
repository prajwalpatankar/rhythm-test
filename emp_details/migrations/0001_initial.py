# Generated by Django 3.1.2 on 2020-10-21 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.IntegerField()),
                ('employee_name', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('date_of_joining', models.DateField()),
                ('mobile', models.CharField(max_length=10)),
                ('email_id', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
            ],
        ),
    ]
