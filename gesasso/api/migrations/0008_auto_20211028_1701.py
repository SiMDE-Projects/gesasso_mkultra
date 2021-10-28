# Generated by Django 3.2.8 on 2021-10-28 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_request_asso'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actiontype',
            name='tasks',
        ),
        migrations.RemoveField(
            model_name='request',
            name='type',
        ),
        migrations.AddField(
            model_name='request',
            name='actions',
            field=models.ManyToManyField(to='api.Action'),
        ),
    ]
