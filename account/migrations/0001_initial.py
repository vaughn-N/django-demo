# Generated by Django 5.0.2 on 2024-02-27 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=25)),
                ('middlename', models.CharField(blank=True, max_length=25, null=True)),
                ('birthdate', models.DateField()),
            ],
        ),
    ]
