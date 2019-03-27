# Generated by Django 2.1.7 on 2019-03-27 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=20)),
                ('lastName', models.CharField(max_length=20)),
                ('Email', models.CharField(max_length=30)),
                ('userName', models.CharField(max_length=20)),
                ('DOB', models.CharField(max_length=15)),
                ('contactNumber', models.IntegerField(max_length=10)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
