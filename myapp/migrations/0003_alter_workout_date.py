# Generated by Django 5.1 on 2024-09-14 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_excersice_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
