# Generated by Django 4.1.1 on 2022-09-16 22:40

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Car_model',
            new_name='Car',
        ),
    ]
