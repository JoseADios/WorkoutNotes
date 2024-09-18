# Generated by Django 5.1 on 2024-09-18 01:05

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_excersice_name_alter_muscle_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workout',
            name='date',
        ),
        migrations.AddField(
            model_name='workout',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
