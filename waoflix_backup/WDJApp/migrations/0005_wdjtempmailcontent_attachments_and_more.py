# Generated by Django 4.1.5 on 2023-01-09 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WDJApp', '0004_wdjtempmailcontent_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='wdjtempmailcontent',
            name='attachments',
            field=models.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='wdjtempmailcontent',
            name='bcc_mails',
            field=models.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='wdjtempmailcontent',
            name='cc_mails',
            field=models.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='wdjtempmailcontent',
            name='from_side',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='wdjcomments',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='wdjcontact',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='wdjtempmailcontent',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='wdjusers',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]