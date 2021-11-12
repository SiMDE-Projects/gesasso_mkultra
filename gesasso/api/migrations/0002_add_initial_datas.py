# Generated by Django 3.2.8 on 2021-10-27 13:12

from django.db import migrations
from django.db.transaction import atomic

from gesasso.api.models import ActionType, TaskType


@atomic
def create_usertypes(apps, schema_editor):
    tt_ssh_reset = TaskType.objects.create(name="Reset SSH password", target="files")
    tt_mysql_reset = TaskType.objects.create(name="Reset MySQL password", target="sql")
    tt_send_mail = TaskType.objects.create(name="Send Mail", target="mail")

    at_allcreds_reset = ActionType.objects.create(name="Reset all credentials")
    at_allcreds_reset.tasks_types.set([tt_ssh_reset, tt_mysql_reset, tt_send_mail])

    at_sshcreds_reset = ActionType.objects.create(name="Reset SSH credentials")
    at_sshcreds_reset.tasks_types.set([tt_ssh_reset, tt_send_mail])

    at_mysqlcreds_reset = ActionType.objects.create(name="Reset MySQL credentials")
    at_mysqlcreds_reset.tasks_types.set([tt_mysql_reset, tt_send_mail])


@atomic
def delete_usertypes(apps, schema_editor):
    ActionType.objects.get(name="Reset all credentials").delete()
    ActionType.objects.get(name="Reset SSH credentials").delete()
    ActionType.objects.get(name="Reset MySQL credentials").delete()

    TaskType.objects.get(name="Reset SSH password").delete()
    TaskType.objects.get(name="Reset MySQL password").delete()
    TaskType.objects.get(name="Send Mail").delete()


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_usertypes, delete_usertypes),
    ]
