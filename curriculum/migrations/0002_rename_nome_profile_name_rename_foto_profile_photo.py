# Generated by Django 5.1.3 on 2024-11-25 00:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='nome',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='foto',
            new_name='photo',
        ),
    ]
