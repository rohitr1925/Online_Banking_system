# Generated by Django 5.0.2 on 2024-04-07 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0006_bus_price_bus_rem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='dest',
        ),
        migrations.RemoveField(
            model_name='book',
            name='source',
        ),
    ]