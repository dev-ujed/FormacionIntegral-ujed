# Generated by Django 3.2.5 on 2024-03-12 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0038_alter_eventos_cveunidadresponsable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventos',
            name='cveUnidadResponsable',
            field=models.CharField(default='', max_length=150, verbose_name='cveunidadResponsable'),
        ),
    ]
