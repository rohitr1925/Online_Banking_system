# Generated by Django 5.0.2 on 2024-04-05 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_remove_bus_nos_remove_bus_price_remove_bus_rem_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bus',
            name='id',
        ),
        migrations.AddField(
            model_name='bus',
            name='bus_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]