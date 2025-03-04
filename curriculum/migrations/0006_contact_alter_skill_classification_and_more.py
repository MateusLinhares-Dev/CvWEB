# Generated by Django 5.1.3 on 2024-11-26 23:07

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0005_skill_points'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, verbose_name='Nome')),
                ('message', models.TextField(verbose_name='Mensagem')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Telofone')),
            ],
            options={
                'verbose_name': 'Contato',
            },
        ),
        migrations.AlterField(
            model_name='skill',
            name='classification',
            field=models.IntegerField(choices=[(1, 'Iniciante'), (2, 'Intermediario'), (3, 'Avancado'), (4, 'Especialista'), (5, 'Master')], default=1, verbose_name='Nivel de conhecimento'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='points',
            field=models.IntegerField(editable=False, verbose_name='Pontuação'),
        ),
    ]
