# Generated by Django 3.2.5 on 2023-11-03 17:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0027_remove_eventos_fechaevento'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventos',
            name='fechaFin',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='fechaFin'),
        ),
        migrations.AddField(
            model_name='eventos',
            name='fechaInicio',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='fechaInicio'),
        ),
    ]
