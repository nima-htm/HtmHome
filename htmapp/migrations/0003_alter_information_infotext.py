# Generated by Django 5.1.7 on 2025-04-07 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('htmapp', '0002_alter_information_infotext'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='infoText',
            field=models.CharField(max_length=100000),
        ),
    ]
