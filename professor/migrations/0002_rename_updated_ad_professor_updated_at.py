# Generated by Django 4.0.4 on 2022-05-16 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('professor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='professor',
            old_name='updated_ad',
            new_name='updated_at',
        ),
    ]