# Generated by Django 5.1 on 2024-09-21 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_alter_setgroup_unique_together'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='setgroup',
            options={'ordering': ['order']},
        ),
        migrations.AlterUniqueTogether(
            name='setgroup',
            unique_together={('workout', 'exercise')},
        ),
    ]
