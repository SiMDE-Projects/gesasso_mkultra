# Generated by Django 3.2.8 on 2021-10-27 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authtoken', '0003_tokenproxy'),
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('api', '0003_auto_20211027_1927'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PortailUser',
        ),
    ]
