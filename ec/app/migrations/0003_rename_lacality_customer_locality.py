# Generated by Django 5.1.2 on 2024-11-05 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='lacality',
            new_name='locality',
        ),
    ]
