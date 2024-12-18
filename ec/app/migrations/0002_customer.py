# Generated by Django 5.1.2 on 2024-11-03 21:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('lacality', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('mobile', models.IntegerField(default=0)),
                ('zipcode', models.IntegerField()),
                ('state', models.CharField(choices=[('Sfax', 'Sfax'), ('Tunis', 'Tunis'), ('Ariana', 'Ariana'), ('BenArous', 'BenArous'), ('Mannouba', 'Mannouba'), ('Bizerte', 'Bizerte'), ('Hammamet', 'Hammamet'), ('Nabeul', 'Nabeul'), ('Sousse', 'Sousse'), ('Monastir', 'Monastir'), ('Mahdia', 'Mahdia'), ('Kaff', 'Kaff'), ('Jandouba', 'Jandouba'), ('Gafsa', 'Gafsa'), ('Sidi-Bouzid', 'Sidi-Bouzid'), ('Karaouin', 'Karaouin'), ('Gasrine', 'Gasrine'), ('Touzeur', 'Touzer'), ('Gbili', 'Gbili'), ('Mednine', 'Mednine'), ('Tataouine', 'Tataouine'), ('Gabes', 'Gabes'), ('Zaghouen', 'Zaghouen'), ('Seliana', 'Seliana')], max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
