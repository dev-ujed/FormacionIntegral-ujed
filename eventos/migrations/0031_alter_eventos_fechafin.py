# Generated by Django 3.2.5 on 2023-11-06 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0030_auto_20231106_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventos',
            name='fechaFin',
            field=models.DateTimeField(blank=True, null=True, verbose_name='fechaFin'),
        ),
    ]
