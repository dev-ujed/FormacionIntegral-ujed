# Generated by Django 3.2.5 on 2024-09-06 20:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0045_alter_eventos_cve_ciclo'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventos',
            name='creacionEvento',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='creacionEvento'),
            preserve_default=False,
        ),
    ]
