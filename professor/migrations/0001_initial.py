# Generated by Django 4.0.4 on 2022-05-12 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('department', models.CharField(choices=[('hist', 'History'), ('math', 'Mathematics'), ('litrt', 'Literature'), ('eng', 'English')], max_length=10)),
                ('time', models.TimeField()),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_ad', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
