# Generated by Django 5.1.6 on 2025-03-05 18:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inicio', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edad', models.IntegerField()),
                ('racha', models.IntegerField(default=0)),
                ('imagen', models.ImageField(default='usuarios/default.jpg', upload_to='usuario/')),
                ('puntos', models.IntegerField(default=0)),
                ('medalla', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inicio.medalla')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
