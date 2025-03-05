# Generated by Django 5.1.6 on 2025-03-05 18:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Insignia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('imagen', models.ImageField(upload_to='insignias/')),
            ],
        ),
        migrations.CreateModel(
            name='Logro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insignia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perfil.insignia')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registro.profile')),
            ],
        ),
    ]
