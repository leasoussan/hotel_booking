# Generated by Django 3.1.4 on 2020-12-27 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0007_auto_20201227_2142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guestsmessage',
            name='guest',
        ),
        migrations.AddField(
            model_name='guestsmessage',
            name='booking',
            field=models.ForeignKey(default=8, on_delete=django.db.models.deletion.CASCADE, to='visitors.booking'),
            preserve_default=False,
        ),
    ]
