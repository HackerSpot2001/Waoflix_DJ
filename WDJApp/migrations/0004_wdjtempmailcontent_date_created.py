# Generated by Django 2.2.12 on 2023-01-08 15:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('WDJApp', '0003_wdjtempmail_wdjtempmailcontent'),
    ]

    operations = [
        migrations.AddField(
            model_name='wdjtempmailcontent',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
