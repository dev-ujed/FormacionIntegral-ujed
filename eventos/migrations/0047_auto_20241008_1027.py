# Generated by Django 3.2.5 on 2024-10-08 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0046_eventos_creacionevento'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventos',
            name='fecha',
            field=models.DateField(blank=True, null=True, verbose_name='fecha'),
        ),
        migrations.AddField(
            model_name='eventos',
            name='hora',
            field=models.TimeField(blank=True, null=True, verbose_name='hora'),
        ),
    ]
