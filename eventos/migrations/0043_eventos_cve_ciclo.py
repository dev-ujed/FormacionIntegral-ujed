# Generated by Django 3.2.5 on 2024-08-15 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0042_remove_eventos_cve_ciclo'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventos',
            name='cve_ciclo',
            field=models.CharField(default='795', max_length=100, verbose_name='cve_ciclo'),
        ),
    ]
