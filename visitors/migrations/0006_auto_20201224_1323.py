# Generated by Django 3.1.4 on 2020-12-24 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0005_auto_20201222_1702'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='rate_night',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='email',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='last_name',
        ),
    ]