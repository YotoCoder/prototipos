# Generated by Django 4.2.1 on 2023-06-01 02:35

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organoleptica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('punto_muestreo', models.CharField(max_length=50)),
                ('presenta_color', models.BooleanField()),
                ('presenta_olor', models.BooleanField()),
                ('presenta_sabor', models.BooleanField()),
                ('particulas_extrañas', models.BooleanField()),
                ('responsable', models.CharField(max_length=50)),
                ('observaciones', ckeditor.fields.RichTextField()),
            ],
        ),
    ]
