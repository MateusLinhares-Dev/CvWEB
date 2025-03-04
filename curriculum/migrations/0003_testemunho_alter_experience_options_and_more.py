# Generated by Django 5.1.3 on 2024-11-25 21:54

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0002_rename_nome_profile_name_rename_foto_profile_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testemunho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('role', models.CharField(blank=True, max_length=100, null=True)),
                ('message', models.TextField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='testemunhos/')),
                ('date_create', models.DateTimeField(default=django.utils.timezone.now)),
                ('confirm', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterModelOptions(
            name='experience',
            options={'verbose_name': 'Experiência'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Perfil'},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': 'Projeto'},
        ),
    ]
