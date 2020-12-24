# Generated by Django 3.1.4 on 2020-12-22 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0004_auto_20201222_0909'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='room_number',
        ),
        migrations.AddField(
            model_name='booking',
            name='room',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='visitors.room'),
            preserve_default=False,
        ),
    ]
