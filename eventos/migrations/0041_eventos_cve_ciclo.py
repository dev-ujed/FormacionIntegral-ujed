# Generated by Django 3.2.5 on 2024-05-13 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0040_alter_eventos_cveunidadresponsable'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventos',
            name='cve_ciclo',
            field=models.CharField(default='795', max_length=100, verbose_name='cve_ciclo'),
        ),
    ]