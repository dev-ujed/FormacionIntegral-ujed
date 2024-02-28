# Generated by Django 3.2.5 on 2024-02-27 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0034_alter_eventos_horas_totales'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventos',
            name='flayer',
            field=models.ImageField(null=True, upload_to='Eventos/images'),
        ),
        migrations.AlterField(
            model_name='eventos',
            name='horas_totales',
            field=models.IntegerField(blank=True, null=True, verbose_name='horas_totales'),
        ),
    ]